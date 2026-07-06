import streamlit as st
import pandas as pd


from src.history import PredictionHistory
from src.footer import footer

# =====================================
# Page Configuration
# =====================================





# =====================================
# Title
# =====================================

st.markdown(
    """
    <h1 class="main-title">
        😊 Emotion Prediction
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="subtitle">
        Enter a sentence below and let the AI predict the emotion.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

@st.cache_resource(show_spinner="Loading AI Models... Please wait (this happens once).")
def get_predictor_v2():
    from src.predict import EmotionPredictor
    return EmotionPredictor()

predictor = get_predictor_v2()

history = PredictionHistory()

# =====================================
# User Input
# =====================================

text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Example: I am very excited today!"
)

st.caption(f"Characters : {len(text)}")

st.divider()

# =====================================
# Buttons
# =====================================

c1, c2 = st.columns(2)

predict = c1.button(
    "🚀 Predict Emotion",
    use_container_width=True
)

clear = c2.button(
    "🗑 Clear",
    use_container_width=True
)

if clear:
    st.rerun()

# =====================================
# Prediction
# =====================================

if predict:

    if text.strip() == "":

        st.warning("Please enter some text.")

    else:

        result = predictor.predict(text)

        emotion = result["emotion"]
        emoji = result["emoji"]
        prediction_time = result["prediction_time"]

        history.save(
            text,
            emotion,
            emoji,
            prediction_time
        )

        st.success("Prediction Completed Successfully!")

        st.divider()

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric(
                "Emotion",
                emotion.title()
            )

        with m2:
            st.metric(
                "Emoji",
                emoji
            )

        with m3:
            st.metric(
                "Prediction Time",
                f"{prediction_time} sec"
            )

        st.divider()

        probability = result["probability"]
        clean_text = result["clean_text"]
        
        st.subheader("🧠 Prediction Insights")
        
        confidence_html = f"""
<div class="insight-card" style="margin-bottom: 20px;">
<div class="insight-card-title">Model Confidence Score</div>
<div class="insight-metric-value" style="font-size: 28px;">{probability}%</div>
<div class="premium-progress-container">
<div class="premium-progress-fill" style="width: {probability}%;"></div>
</div>
<div style="font-size: 13px; color: #6B7280; margin-top: 10px;">The AI model is {probability}% confident in the "{emotion}" classification.</div>
</div>
"""
        st.markdown(confidence_html, unsafe_allow_html=True)
        
        nlp_html = f"""
<div class="insight-card">
<div class="insight-card-title">NLP Text Breakdown</div>
<div class="insight-metric-group">
<span class="insight-metric-label">Original Text Length</span>
<span class="insight-metric-value">{len(text)} <span style="font-size:14px; font-weight:500; color:#6B7280">chars</span></span>
</div>
<div class="insight-metric-group">
<span class="insight-metric-label">Cleaned Text Length</span>
<span class="insight-metric-value">{len(clean_text)} <span style="font-size:14px; font-weight:500; color:#6B7280">chars</span></span>
</div>
<div style="margin-top: 20px;">
<span class="insight-metric-label" style="display:block; margin-bottom:10px;">What the AI Analyzed:</span>
<div class="insight-code-block">{clean_text if clean_text.strip() else "[Empty after cleaning]"}</div>
</div>
</div>
"""
        st.markdown(nlp_html, unsafe_allow_html=True)

        summary = pd.DataFrame({
            "Input Text": [text],
            "Cleaned Text": [clean_text],
            "Emotion": [emotion],
            "Emoji": [emoji],
            "Confidence (%)": [probability],
            "Prediction Time (sec)": [prediction_time]
        })

        st.download_button(
            label="📥 Download Prediction",
            data=summary.to_csv(index=False),
            file_name="prediction.csv",
            mime="text/csv"
        )

footer()
