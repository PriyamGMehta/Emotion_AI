import streamlit as st
import pandas as pd


from src.footer import footer

# ============================================
# Page Configuration
# ============================================





# ============================================
# Title
# ============================================

st.title("📂 Batch Emotion Prediction")

st.write(
    "Upload a CSV file containing a 'text' column to predict emotions in bulk."
)

st.divider()

@st.cache_resource(show_spinner="Loading AI Models... Please wait (this happens once).")
def get_predictor():
    from src.predict import EmotionPredictor
    return EmotionPredictor()

predictor = get_predictor()

# ============================================
# File Upload
# ============================================

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

st.divider()

# ============================================
# Prediction Logic
# ============================================

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    if "text" not in df.columns:

        st.error("CSV file must contain a 'text' column.")

    else:

        st.success("File uploaded successfully!")

        if st.button("🚀 Start Batch Prediction"):

            with st.spinner("Predicting emotions..."):

                predictions = []
                emojis = []
                times = []

                for text in df["text"]:

                    result = predictor.predict(str(text))

                    predictions.append(result["emotion"])
                    emojis.append(result["emoji"])
                    times.append(result["prediction_time"])

                df["predicted_emotion"] = predictions
                df["emoji"] = emojis
                df["prediction_time_sec"] = times

            st.success("Batch Prediction Completed!")

            st.divider()

            # ============================================
            # Display Results
            # ============================================

            st.subheader("📄 Prediction Results")

            st.dataframe(
                df,
                use_container_width=True,
                height=400
            )

            st.divider()

            # ============================================
            # Download Results
            # ============================================

            st.download_button(
                label="📥 Download Results",
                data=df.to_csv(index=False),
                file_name="batch_prediction_results.csv",
                mime="text/csv"
            )

st.divider()

footer()
