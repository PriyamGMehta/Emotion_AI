import streamlit as st
import pandas as pd
import base64

from src.dashboard_utils import DashboardUtils
from src.footer import footer

@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ==============================
# Load Dataset
# ==============================

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/train_clean.csv")

df = load_data()
dashboard = DashboardUtils()

# ==============================
# Neural Core Interface
# ==============================

total_samples = len(df)
emotion_classes = df["emotion"].nunique()
vocabulary = df["clean_text"].str.split().explode().nunique()
average_length = round(df["clean_text"].str.split().apply(len).mean(), 2)

banner_base64 = get_base64_of_bin_file("app/assets/neural_core_banner.png")

st.markdown(f"""
<div class="neural-banner-container">
<img src="data:image/png;base64,{banner_base64}" class="neural-banner-img" />
<div class="neural-metrics-overlay">
<div class="neural-glass-metric">
<div class="neural-value">{total_samples:,}</div>
<div class="neural-label">Training Samples</div>
</div>
<div class="neural-glass-metric">
<div class="neural-value">{emotion_classes}</div>
<div class="neural-label">Emotion Classes</div>
</div>
<div class="neural-glass-metric">
<div class="neural-value">{vocabulary:,}</div>
<div class="neural-label">Vocabulary Size</div>
</div>
<div class="neural-glass-metric">
<div class="neural-value">{average_length}</div>
<div class="neural-label">Avg Sentence Len</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# ==============================
# Tabbed Interface
# ==============================

tab1, tab2 = st.tabs(["📈 Analytics & Trends", "🗂️ Dataset Explorer"])

# --------- TAB 1: ANALYTICS ---------
with tab1:
    st.markdown("### Performance & Distribution")
    st.write("Visual breakdown of the dataset's class distribution.")
    
    left, right = st.columns(2)
    with left:
        st.plotly_chart(
            dashboard.emotion_bar_chart(df),
            use_container_width=True
        )
    with right:
        st.plotly_chart(
            dashboard.emotion_pie_chart(df),
            use_container_width=True
        )

# --------- TAB 2: DATA EXPLORER ---------
with tab2:
    st.markdown("### Emotion Class Counts")
    
    emotion_count = df["emotion"].value_counts().reset_index()
    emotion_count.columns = ["Emotion", "Count"]
    max_count = emotion_count["Count"].max()
    
    progress_html = "<div class='feed-container'>"
    for _, row in emotion_count.iterrows():
        emotion = row["Emotion"]
        count = row["Count"]
        percentage = (count / max_count) * 100
        
        progress_html += f"""
<div class="progress-strip-container">
<div class="progress-header">
<span style="text-transform: capitalize;">{emotion}</span>
<span>{count:,}</span>
</div>
<div class="progress-track">
<div class="progress-fill fill-{emotion}" style="width: {percentage}%;"></div>
</div>
</div>
"""
    progress_html += "</div>"
    st.markdown(progress_html, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Dataset Feed (Top 50)")
    
    feed_html = "<div class='feed-container'>"
    for _, row in df.head(50).iterrows():
        text = row["clean_text"]
        emotion = row["emotion"]
        
        # Handle cases where text might be too long or empty
        display_text = text if isinstance(text, str) else "No text data"
        
        feed_html += f"""
<div class="feed-row">
<div class="feed-text" title="{display_text}">{display_text}</div>
<div class="emotion-pill pill-{emotion}">{emotion}</div>
</div>
"""
    feed_html += "</div>"
    
    st.markdown(feed_html, unsafe_allow_html=True)


# ==============================
# Footer
# ==============================
footer()
