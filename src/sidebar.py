import streamlit as st
import sys

# ==========================================
# Patch for PyTorch + Streamlit File Watcher
# ==========================================
try:
    import torch
    if hasattr(torch.classes, "__path__"):
        torch.classes.__path__ = []
except ImportError:
    pass


def load_css():
    with open("app/assets/style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )

def render_sidebar():
    load_css()
    with st.sidebar:
        
        # Mac OS Dots
        st.markdown('<div class="sidebar-mac-dots"></div>', unsafe_allow_html=True)
        
        # Brand Logo and Title
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("app/assets/logo.png", width=30)
        with col2:
            st.markdown("<h3 style='color: white; margin: 0; padding-top: 5px; font-size: 18px;'>Emotion AI</h3>", unsafe_allow_html=True)
            
        st.write("")
        

        
        # Custom Navigation (Replaces Native)
        st.page_link("app.py", label="Home", icon="🏠")
        st.page_link("pages/1_Dashboard.py", label="Dashboard", icon="📊")
        st.page_link("pages/2_Predict.py", label="Predict", icon="😊")
        st.page_link("pages/3_Dataset.py", label="Dataset", icon="📁")
        st.page_link("pages/4_Analytics.py", label="Analytics", icon="📈")
        st.page_link("pages/5_Model_Comparison.py", label="Models", icon="🤖")
        st.page_link("pages/6_About.py", label="About", icon="ℹ️")
        st.page_link("pages/7_Prediction_History.py", label="History", icon="📜")
        st.page_link("pages/8_Batch_Prediction.py", label="Batch Prediction", icon="📂")

