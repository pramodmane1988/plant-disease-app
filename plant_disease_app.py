import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Plant Disease Detector", layout="centered")

st.title("🌿 Real-Time Plant Disease Detection App")
st.write("Upload a leaf image and get instant disease prediction.")

# Dummy model (replace with real model later)
def predict(image):
    diseases = ["Healthy", "Rust", "Red Rot", "Blight"]
    return np.random.choice(diseases)

uploaded_file = st.file_uploader("📤 Upload Leaf Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Diagnose Disease"):
        result = predict(image)
        st.success(f"🌱 **Result:** {result}")
