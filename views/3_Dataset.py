import streamlit as st
import pandas as pd

from src.footer import footer

# ============================================
# Page Configuration
# ============================================



# ============================================
# Load Dataset
# ============================================

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/train_clean.csv")

df = load_data()

# ============================================
# Title
# ============================================

st.markdown(
    """
    <h1 class="main-title">
        📁 Dataset Explorer
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="subtitle">
        Explore, search and filter the processed emotion dataset.
    </p>
    """,
    unsafe_allow_html=True
)


# ============================================
# Search & Filter
# ============================================

left, right = st.columns(2)

with left:

    search = st.text_input(
        "🔍 Search Text"
    )

with right:

    emotion = st.selectbox(
        "🎭 Select Emotion",
        ["All"] + sorted(
            df["emotion"].unique()
        )
    )

# ============================================
# Apply Filters
# ============================================

filtered_df = df.copy()

if search:

    filtered_df = filtered_df[
        filtered_df["text"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

if emotion != "All":

    filtered_df = filtered_df[
        filtered_df["emotion"] == emotion
    ]

st.success(
    f"Showing {len(filtered_df)} records"
)

st.divider()

# ============================================
# Dataset Table
# ============================================

st.subheader("📄 Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=500
)

st.divider()

# ============================================
# Download Dataset
# ============================================

st.download_button(
    label="📥 Download Filtered Dataset",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_dataset.csv",
    mime="text/csv"
)

st.divider()

# ============================================
# Emotion Summary
# ============================================

st.subheader("📊 Emotion Distribution")

emotion_summary = (
    filtered_df["emotion"]
    .value_counts()
    .reset_index()
)

emotion_summary.columns = [
    "Emotion",
    "Count"
]

st.dataframe(
    emotion_summary,
    use_container_width=True
)

footer()
