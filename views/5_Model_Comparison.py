import streamlit as st

from src.model_comparison import ModelComparison
from src.footer import footer

# ============================================
# Page Configuration
# ============================================



comparison = ModelComparison()

df = comparison.get_data()

best = comparison.best_model()

# ============================================
# Title
# ============================================

st.title("🤖 Machine Learning Model Comparison")

st.write(
    "Compare the performance of all trained machine learning models."
)

st.divider()

# ============================================
# Best Model Metrics
# ============================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🏆 Best Model",
        best["Model"]
    )

with c2:
    st.metric(
        "Accuracy",
        f"{best['Accuracy']:.4f}"
    )

with c3:
    st.metric(
        "Precision",
        f"{best['Precision']:.4f}"
    )

with c4:
    st.metric(
        "F1 Score",
        f"{best['F1 Score']:.4f}"
    )

st.divider()

# ============================================
# Charts
# ============================================

left, right = st.columns(2)

with left:

    st.plotly_chart(
        comparison.accuracy_chart(),
        use_container_width=True
    )

with right:

    st.plotly_chart(
        comparison.precision_chart(),
        use_container_width=True
    )

left, right = st.columns(2)

with left:

    st.plotly_chart(
        comparison.recall_chart(),
        use_container_width=True
    )

with right:

    st.plotly_chart(
        comparison.f1_chart(),
        use_container_width=True
    )

st.divider()

# ============================================
# Model Comparison Table
# ============================================

st.subheader("📋 Performance Comparison")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

footer()
