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

def make_metric(label, value):
    return f"""
<div class="insight-card" style="padding: 15px;">
<div style="color: #6B7280; font-size: 13px; font-weight: 600; text-transform: uppercase; margin-bottom: 5px;">{label}</div>
<div style="color: #1F2937; font-size: 24px; font-weight: 800;">{value}</div>
</div>
"""

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(make_metric("Total Samples", stats["Total Samples"]), unsafe_allow_html=True)
with c2:
    st.markdown(make_metric("Emotion Classes", stats["Emotion Classes"]), unsafe_allow_html=True)
with c3:
    st.markdown(make_metric("Vocabulary Size", stats["Vocabulary Size"]), unsafe_allow_html=True)
with c4:
    st.markdown(make_metric("Avg Sentence Length", stats["Average Sentence Length"]), unsafe_allow_html=True)

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

from src.emoji_mapper import EMOJI_MAP

feed_html = '<div class="feed-container">'
for _, row in df.head(50).iterrows():
    text = str(row['clean_text']) if pd.notna(row['clean_text']) else ""
    emotion = str(row['emotion']).lower()
    emoji = EMOJI_MAP.get(emotion, "❓")
    
    feed_html += f"""
<div class="feed-row">
<div style="font-size: 14px; color: #374151; font-weight: 500; max-width: 80%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
"{text}"
</div>
<div class="emotion-pill emotion-{emotion}">
{emoji} {emotion.capitalize()}
</div>
</div>
"""
feed_html += '</div>'

st.markdown(feed_html, unsafe_allow_html=True)

footer()
