import streamlit as st

from src.footer import footer

# ============================================
# Page Configuration
# ============================================



# ============================================
# Title
# ============================================

st.title("ℹ️ About Emotion AI")

st.write(
    "AI Powered Emotion Detection System using Natural Language Processing and Machine Learning."
)

st.divider()

# ============================================
# Project Overview
# ============================================

st.header("📖 Project Overview")

st.write("""
Emotion AI is an NLP-based application that detects human emotions from text.

The system preprocesses user text, converts it into numerical features using
TF-IDF Vectorization, predicts the emotion using Machine Learning models,
and displays the detected emotion along with an emoji.
""")

st.divider()

# ============================================
# Objective
# ============================================

st.header("🎯 Project Objectives")

st.markdown("""
- Detect emotions from textual data.
- Compare multiple Machine Learning models.
- Provide real-time emotion prediction.
- Perform batch prediction using CSV files.
- Visualize dataset insights using interactive charts.
""")

st.divider()

# ============================================
# Dataset
# ============================================

st.header("📊 Dataset")

st.write("""
Dataset Used:

Emotion Dataset for NLP

The dataset contains text samples categorized into multiple emotion classes.
""")

st.divider()

# ============================================
# Machine Learning Models
# ============================================

st.header("🤖 Machine Learning Models")

models = [
    "Logistic Regression",
    "Naive Bayes",
    "Decision Tree",
    "Random Forest",
    "Linear SVM"
]

for model in models:
    st.write(f"✅ {model}")

st.divider()

# ============================================
# Technologies
# ============================================

st.header("🛠 Technologies Used")

left, right = st.columns(2)

with left:

    st.markdown("""
### Programming

- Python

### NLP

- spaCy
- NLTK

### ML

- Scikit-Learn
""")

with right:

    st.markdown("""
### Visualization

- Plotly
- Matplotlib
- WordCloud

### Web

- Streamlit

### Data

- Pandas
- NumPy
""")

st.divider()

# ============================================
# Workflow
# ============================================

st.header("🔄 Workflow")

st.markdown("""
Dataset

⬇️

Data Preprocessing

⬇️

Feature Engineering (TF-IDF)

⬇️

Model Training

⬇️

Model Evaluation

⬇️

Emotion Prediction

⬇️

Streamlit Web Application
""")

st.divider()

# ============================================
# Developer
# ============================================

st.header("👨‍💻 Developer")

st.info("""
**Name:** Priyam Mehta

**Internship:** Intellect

**Project:** Emotion AI

**Technology:** NLP + Machine Learning + Streamlit
""")

st.divider()

# ============================================
# Future Scope
# ============================================

st.header("🚀 Future Enhancements")

st.markdown("""
- Deep Learning Models (LSTM, BERT)
- Voice Emotion Recognition
- Multilingual Emotion Detection
- Emotion Trend Dashboard
- API Deployment
- Mobile Application
""")

footer()
