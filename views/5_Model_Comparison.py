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

st.markdown(
    """
    <h1 class="main-title">
        🤖 Model Intelligence
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="subtitle">
        Evaluate and compare the performance of all trained machine learning models.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ============================================
# Champion Model Banner
# ============================================

st.markdown(f"""
<div class="champion-banner">
    <div class="champion-header">
        <span class="champion-badge">🏆 Champion Model</span>
    </div>
    <div class="champion-model-name">{best['Model']}</div>
    <div class="champion-metrics">
        <div class="champion-metric-box">
            <div class="champion-metric-value">{best['Accuracy']:.4f}</div>
            <div class="champion-metric-label">Accuracy</div>
        </div>
        <div class="champion-metric-box">
            <div class="champion-metric-value">{best['Precision']:.4f}</div>
            <div class="champion-metric-label">Precision</div>
        </div>
        <div class="champion-metric-box">
            <div class="champion-metric-value">{best['Recall']:.4f}</div>
            <div class="champion-metric-label">Recall</div>
        </div>
        <div class="champion-metric-box">
            <div class="champion-metric-value">{best['F1 Score']:.4f}</div>
            <div class="champion-metric-label">F1 Score</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# Performance Bar Chart Analysis
# ============================================

st.plotly_chart(
    comparison.grouped_bar_chart(),
    use_container_width=True
)

st.divider()

# ============================================
# Model Comparison Table
# ============================================

st.subheader("📋 Detailed Performance Metrics")

# Styling the dataframe to highlight the maximum values in each column
styled_df = df.style.highlight_max(
    subset=['Accuracy', 'Precision', 'Recall', 'F1 Score'],
    color='#3B82F6',
    axis=0
).format(
    {
        'Accuracy': '{:.4f}',
        'Precision': '{:.4f}',
        'Recall': '{:.4f}',
        'F1 Score': '{:.4f}'
    }
)

st.dataframe(
    styled_df,
    use_container_width=True
)

st.divider()

footer()
