
# Product Story Generation System

This repository contains the implementation of a system for generating product stories from various text files containing product-related data. The system identifies patterns, extracts themes, and generates actionable insights to assist product teams.

## **Overview**

The system performs the following tasks:
1. **Content Analysis:** Extracts summaries of documents and identifies common themes using Seeded LDA.
2. **Theme Refinement:** Uses a prompt-tuned LLM to refine extracted themes into concise labels.
3. **Document Clustering:** Tags each document with its theme and clusters them using KMeans and other clustering algorithms.
4. **Story Generation:** Leverages tagged clusters and few-shot learning to generate coherent product stories.

## **Workflow**

1. **Content Analysis**:
   - Extracts summaries of all documents.
   - Applies Seeded LDA to identify key themes and common words.
   - Reads a comparative study of Seeded LDA vs. prompt-tuned LLMs for theme refinement.

2. **Theme Refinement**:
   - Defines prompts for the LLM to exclude irrelevant words identified by LDA.
   - Generates concise themes in less than three words.

3. **Clustering**:
   - Tags documents with their respective themes.
   - Groups documents into clusters using KMeans and other clustering algorithms.

4. **Story Generation**:
   - Uses clustered documents to create product stories.
   - Employs few-shot learning techniques for crafting narratives.

5. **Output**:
   - Final stories include the story type (Concern, Win, Insight, or Opportunity), actionable insights, and relevant data with citations.

## **Features**

- **Automated Theme Extraction:** Combines Seeded LDA and prompt-tuned LLM for theme identification.
- **Clustering:** Efficiently groups documents based on extracted themes.
- **Story Generation:** Produces concise, data-driven narratives with actionable insights.
- **Scalable Architecture:** Designed to handle diverse datasets and scale with additional sources.

## **Documentation**

### **Content Analysis**
- Summarizes documents and identifies initial themes using Seeded LDA.
- Refines themes with prompt-tuned LLMs for better accuracy and relevance.

### **Story Generation**
- Tags documents with cluster labels.
- Uses few-shot learning to generate coherent and actionable product stories.

### **Methodology**
- Combines statistical methods (LDA) with LLMs for robust theme extraction.
- Uses clustering to associate documents with specific themes.

## **Sample Output**

Generated stories include:
1. **Story Type:** Concern, Win, Insight, or Opportunity.
2. **Actionable Insights:** Data-driven recommendations for the product team.
3. **Source Citations:** References to relevant input files.

## **Future Improvements**

- Incorporate automation of workflow while fetching real time data.
- Explore alternative clustering algorithms for better accuracy.
- Fine-tune LLMs for enhanced storytelling.

## **Demo**
<video src='demo.mp4' width=180/>   

---
