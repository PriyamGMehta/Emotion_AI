import streamlit as st

from src.footer import footer

# ============================================
# Page Configuration
# ============================================



# ============================================
# Title
# ============================================

st.title("⚙️ Application Settings")

st.write("Configure the application preferences.")

st.divider()

# ============================================
# Theme Settings
# ============================================

st.header("🎨 Theme")

theme = st.radio(
    "Select Theme Mode",
    ["System Default", "Light Mode", "Dark Mode"],
    index=0
)

st.info("Theme changes will be applied on the next reload.")

st.divider()

# ============================================
# Developer Mode
# ============================================

st.header("👨‍💻 Developer Mode")

dev_mode = st.toggle("Enable Developer Mode")

if dev_mode:
    st.success("Developer mode enabled!")
    
    st.subheader("🔧 Debug Information")
    st.write({
        "Streamlit Version": st.__version__,
        "Python Version": "3.11",
        "Environment": "Production"
    })

st.divider()

# ============================================
# Notifications
# ============================================

st.header("🔔 Notifications")

st.checkbox("Enable Browser Notifications", value=True)
st.checkbox("Show Toast Messages", value=True)

st.divider()

# ============================================
# Reset
# ============================================

st.header("⚠️ Reset Application")

st.warning("This will clear all session states and reload the application.")

if st.button("🔄 Reset App", use_container_width=True):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.rerun()

st.divider()

footer()
