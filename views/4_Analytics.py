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

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Samples", stats["Total Samples"])
c2.metric("Emotion Classes", stats["Emotion Classes"])
c3.metric("Vocabulary Size", stats["Vocabulary Size"])
c4.metric("Average Sentence Length", stats["Average Sentence Length"])

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

# ==========================================
# Dataset Preview
# ==========================================

st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

footer()
