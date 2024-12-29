import streamlit as st
import pandas as pd
import ollama  # Ensure this package is installed and configured

df = pd.read_csv("final_result.csv")  # Update with your dataset path

def generate_story_from_summary_and_topic(text):
    prompt = f"""
    You are a creative writing assistant and journalist. Your task is to write a cohesive, professional report based on the topics and summaries provided. The report should:
    - Be well-structured and follow a clear narrative arc.
    - Integrate relevant values, dates, metrics, or key insights seamlessly into the story.
    - Maintain a formal tone and professionalism throughout in 200-300 words.

    Incorporate key elements from the provided topics and summaries, ensuring clarity and logical progression. Where applicable, include actionable recommendations or insights. Follow the structure of the provided example below:

    Example:
    **Headline**: Video Quality Concerns Impact Rural Therapy Sessions

    **Introduction**:
    Recent analysis reveals significant challenges with video quality in rural areas, affecting therapy session effectiveness. According to product_metrics.txt, 40% of rural users experience video freezing during sessions, with peak issues occurring during high-traffic hours (2-4 PM EST).

    **Key Findings**:
    - **Impact on Therapeutic Care**: Patient feedback indicates serious clinical implications. session_transcripts.txt shows 28% of affected sessions required rescheduling, while progress_notes.txt reveals therapists report "significant disruption in therapeutic momentum" during critical moments.
    - **Patient Feedback**: Analysis of interview_transcripts.txt highlights patient frustration, with 65% mentioning connectivity as a primary concern.
    - **Technical Analysis**: Investigation of jira_tickets.txt indicates the root cause lies in bandwidth optimization. Current system requires 2.5Mbps stable connection, while user_journey.txt data shows rural users average 1.8Mbps during peak hours. feature_specs.txt suggests potential for adaptive bitrate implementation.

    **Recommendations**:
    1. Implement adaptive bitrate streaming (product_requirements.txt).
    2. Add offline mode for progress notes (feedback_analysis.txt).
    3. Develop automated session recovery protocol (design_mockup.txt).

    Based on this example, generate a report using the information below:

    {text}

    Provide the output in the following format:
    **Headline**: [Your Headline]
    **Introduction**: [Your Introduction]
    **Key Findings**:
    - [Finding 1]
    - [Finding 2]
    ...
    **Recommendations**:
    1. [Recommendation 1]
    2. [Recommendation 2]
    ...
    """
    response = ollama.chat(model='llama3.1', messages=[
            {"role": "system", "content": "You are a story-writing assistant."},
            {"role": "user", "content": prompt}
        ])
    return response['message']['content']

def classify_story(story):
    prompt = f"""
    You are a story analysis assistant. Read the following story and classify it into one of the four categories: 
    - INSIGHT: The story provides a deep understanding or realization.
    - OPPORTUNITY: The story highlights a chance for growth or a new possibility.
    - WIN: The story reflects a positive outcome or success.
    - CONCERN: The story raises a potential problem, issue, or danger.

    Story:
    {story}

    Based on the content, classify the story into one of the categories and explain your reasoning briefly:
    - Category: [INSIGHT/OPPORTUNITY/WIN/CONCERN]
    - Reason:
    """
    response = ollama.chat(model='llama3.1', messages=[
        {"role": "system", "content": "You are a story analysis assistant."},
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']

# Streamlit App
st.title("Story Generator and Classifier App")

# Initialize session state
if "generated_story" not in st.session_state:
    st.session_state["generated_story"] = ""

# Input for cluster label
cluster_label = st.number_input("Enter a cluster label (0-4):", min_value=0, max_value=4, step=1)

# Filter data based on cluster label
cluster_data = df[df['Cluster'] == cluster_label]

# Combine summaries and topics
combined = " ".join(
    f"Topic: {row['topic']}\nSummary: {row['output']}"
    for _, row in cluster_data.iterrows()
)

# Buttons for generating story and classifying
if st.button("Generate Story"):
    if combined.strip():
        with st.spinner("Generating story..."):
            story = generate_story_from_summary_and_topic(combined)
            references_section = "\n**References**:\n" + "\n".join(f"- {file}" for file in cluster_data['file_name'])
            story_with_references = story + "\n" + references_section
            st.session_state["generated_story"] = story_with_references
        st.subheader("Generated Story")
        st.write(st.session_state["generated_story"])
    else:
        st.warning(f"No summaries or topics found for Cluster {cluster_label}.")

if st.button("Classify Story"):
    if st.session_state["generated_story"]:
        with st.spinner("Classifying story..."):
            classification = classify_story(st.session_state["generated_story"])
        st.subheader("Story Classification")
        st.write(classification)
    else:
        st.warning("Please generate a story first before classification.")
