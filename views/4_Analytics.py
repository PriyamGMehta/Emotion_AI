import streamlit as st
import pandas as pd

from src.analytics import Analytics
from src.footer import footer

# ==========================================
# Page Configuration
# ==========================================



# ==========================================
# Load Dataset
# ==========================================

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/train_clean.csv")

df = load_data()

analytics = Analytics()

# ==========================================
# Title
# ==========================================

st.title("📈 Analytics Dashboard")

st.write(
    "Explore interactive analytics of the Emotion Dataset."
)

st.divider()

# ==========================================
# Statistics
# ==========================================

@st.cache_data
def get_emotion_stats(_df):
    return analytics.emotion_statistics(_df)

stats = get_emotion_stats(df)

inline_stats = f"""
<div style="text-align: center; color: #6B7280; font-size: 15px; font-weight: 500; margin-bottom: 30px; letter-spacing: 0.5px;">
    <span style="color: #2563EB; font-weight: 700;">{stats['Total Samples']:,}</span> Total Samples 
    <span style="margin: 0 15px; color: #D1D5DB;">|</span> 
    <span style="color: #2563EB; font-weight: 700;">{stats['Emotion Classes']}</span> Emotion Classes 
    <span style="margin: 0 15px; color: #D1D5DB;">|</span> 
    <span style="color: #2563EB; font-weight: 700;">{stats['Vocabulary Size']:,}</span> Vocabulary Size 
    <span style="margin: 0 15px; color: #D1D5DB;">|</span> 
    <span style="color: #2563EB; font-weight: 700;">{stats['Average Sentence Length']}</span> Avg Sentence Length
</div>
"""
st.markdown(inline_stats, unsafe_allow_html=True)

st.divider()

# ==========================================
# Emotion Charts
# ==========================================

left, right = st.columns(2)

@st.cache_data
def get_emotion_dist(_df):
    return analytics.emotion_distribution(_df)

@st.cache_data
def get_emotion_pie(_df):
    return analytics.emotion_pie_chart(_df)

with left:
    st.plotly_chart(
        get_emotion_dist(df),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        get_emotion_pie(df),
        use_container_width=True
    )

st.divider()

# ==========================================
# Sentence Length
# ==========================================

st.subheader("📏 Sentence Length Distribution")

@st.cache_data
def get_sentence_length(_df):
    return analytics.sentence_length_distribution(_df)

st.plotly_chart(
    get_sentence_length(df),
    use_container_width=True
)

st.divider()

# ==========================================
# Top Words
# ==========================================

st.subheader("🔤 Top 20 Frequent Words")

@st.cache_data
def get_top_words(_df):
    return analytics.top_words(_df)

st.plotly_chart(
    get_top_words(df),
    use_container_width=True
)

st.divider()



footer()
