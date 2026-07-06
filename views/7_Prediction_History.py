import streamlit as st

from src.history import PredictionHistory
from src.footer import footer

# ============================================
# Page Configuration
# ============================================



history = PredictionHistory()
df = history.load()

# ============================================
# Title
# ============================================

st.title("📜 Prediction History")

st.write("View all your past predictions.")

st.divider()

# ============================================
# History Data
# ============================================

if df.empty:

    st.info("No prediction history found.")

else:

    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.download_button(
            label="📥 Download History",
            data=df.to_csv(index=False),
            file_name="prediction_history.csv",
            mime="text/csv",
            use_container_width=True
        )

    with c2:

        clear = st.button(
            "🗑 Clear History",
            use_container_width=True
        )

        if clear:
            history.clear()
            st.rerun()

st.divider()

footer()
