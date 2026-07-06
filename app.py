import streamlit as st

st.set_page_config(
    page_title="Emotion AI",
    page_icon="😊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Patch for PyTorch + Streamlit File Watcher
# ==========================================
try:
    import torch
    if hasattr(torch.classes, "__path__"):
        torch.classes.__path__ = []
except ImportError:
    pass

# ==========================================
# Load Global CSS & Fonts
# ==========================================
st.markdown(
    """<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700;900&display=swap" rel="stylesheet">""",
    unsafe_allow_html=True
)

with open("app/assets/style.css", encoding="utf-8") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# Navigation Configuration
# ==========================================
pages = [
    st.Page("src/home_page.py", title="Home", icon="🏠"),
    st.Page("views/1_Dashboard.py", title="Dashboard", icon="📊"),
    st.Page("views/2_Predict.py", title="Predict", icon="😊"),
    st.Page("views/3_Dataset.py", title="Dataset", icon="📁"),
    st.Page("views/4_Analytics.py", title="Analytics", icon="📈"),
    st.Page("views/5_Model_Comparison.py", title="Models", icon="🤖"),
    st.Page("views/7_Prediction_History.py", title="History", icon="📜"),
    st.Page("views/8_Batch_Prediction.py", title="Batch Prediction", icon="📂"),
    st.Page("views/6_About.py", title="About", icon="ℹ️")
]

pg = st.navigation(pages, position="hidden")

# ==========================================
# Sidebar Branding and Custom Navigation
# ==========================================
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
    
    # Custom Navigation
    st.page_link("src/home_page.py", label="Home", icon="🏠")
    st.page_link("views/1_Dashboard.py", label="Dashboard", icon="📊")
    st.page_link("views/2_Predict.py", label="Predict", icon="😊")
    st.page_link("views/3_Dataset.py", label="Dataset", icon="📁")
    st.page_link("views/4_Analytics.py", label="Analytics", icon="📈")
    st.page_link("views/5_Model_Comparison.py", label="Models", icon="🤖")
    st.page_link("views/7_Prediction_History.py", label="History", icon="📜")
    st.page_link("views/8_Batch_Prediction.py", label="Batch Prediction", icon="📂")
    st.page_link("views/6_About.py", label="About", icon="ℹ️")

pg.run()
