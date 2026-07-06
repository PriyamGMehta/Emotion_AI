import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Convert image to base64 to use in HTML
img_b64 = get_base64_of_bin_file("app/assets/hero.png")

# ===========================
# Hero Section
# ===========================

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

left_col, right_col = st.columns([1.2, 1], gap="large")

with left_col:
    st.markdown(
        """
        <div style="padding-top: 40px;">
            <div class="hero-title">
                Understand Human Emotions with AI
            </div>
            <div class="hero-subtitle">
                Unlock the power of Natural Language Processing and Machine Learning to detect, analyze, and visualize emotions from text in real-time.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    b1, b2 = st.columns([1, 1])
    with b1:
        st.page_link("views/2_Predict.py", label="🚀 Start Predicting", use_container_width=True)
    with b2:
        st.page_link("views/1_Dashboard.py", label="📊 View Dashboard", use_container_width=True)

with right_col:
    st.markdown(
        f"""
        <div style="text-align: right;">
            <img src="data:image/png;base64,{img_b64}" class="hero-image" alt="AI Emotion Brain">
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ===========================
# Features Section
# ===========================

st.markdown("## ✨ Key Features")
st.write("Explore the powerful tools built into the Emotion Detection System.")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="glass-card">
        <div class="glass-icon">📊</div>
        <div class="glass-title">Interactive Dashboard</div>
        <div class="glass-desc">Visualize deep dataset metrics and performance analytics instantly.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <div class="glass-icon">🤖</div>
        <div class="glass-title">Model Comparison</div>
        <div class="glass-desc">Compare cutting-edge ML models to find the absolute best fit.</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass-card">
        <div class="glass-icon">😊</div>
        <div class="glass-title">Emotion Prediction</div>
        <div class="glass-desc">Instantly detect and classify emotions from any input text.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="glass-icon">📁</div>
        <div class="glass-title">Dataset Explorer</div>
        <div class="glass-desc">Search, filter, and seamlessly analyze raw text data.</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="glass-card">
        <div class="glass-icon">📂</div>
        <div class="glass-title">Batch Prediction</div>
        <div class="glass-desc">Upload large CSV files for lightning-fast bulk emotion processing.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="glass-icon">📜</div>
        <div class="glass-title">Prediction History</div>
        <div class="glass-desc">Keep track of all your past predictions and history securely.</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ===========================
# Core Workflow
# ===========================

st.markdown("## 🧠 Core Workflow")
st.write("How our Emotion AI model learns and predicts behind the scenes.")

st.markdown("""
<div class="timeline-container">
<div class="timeline-step">
<div class="timeline-icon">📁</div>
<div class="timeline-title">Dataset</div>
</div>
<div class="timeline-arrow">➔</div>

<div class="timeline-step">
<div class="timeline-icon">⚙️</div>
<div class="timeline-title">Preprocess</div>
</div>
<div class="timeline-arrow">➔</div>

<div class="timeline-step">
<div class="timeline-icon">🔢</div>
<div class="timeline-title">Vectorize</div>
</div>
<div class="timeline-arrow">➔</div>

<div class="timeline-step">
<div class="timeline-icon">🤖</div>
<div class="timeline-title">ML Model</div>
</div>
<div class="timeline-arrow">➔</div>

<div class="timeline-step">
<div class="timeline-icon">✨</div>
<div class="timeline-title">Prediction</div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("Developed by Priyam Mehta | Intellect Internship Project")