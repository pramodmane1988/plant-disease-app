import streamlit as st
from PIL import Image, ImageEnhance
import numpy as np
import cv2

st.set_page_config(page_title="Plant Disease Detector", layout="centered")

st.title("🌿 Real-Time Plant Disease Detection App")
st.write("Upload a leaf image and get instant disease prediction.")

# -------- Image Preprocessing --------
def preprocess_image(image):
    # Convert PIL image to OpenCV format
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Resize to standard size (model-friendly)
    img = cv2.resize(img, (224, 224))

    # Noise reduction
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # Contrast enhancement
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.equalizeHist(l)
    enhanced = cv2.merge((l, a, b))
    img = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)

    # Normalize
    img = img / 255.0

    return img

# -------- Dummy Model (Replace Later) --------
def predict(image_array):
    diseases = ["Healthy", "Rust", "Red Rot", "Blight"]
    confidence = round(np.random.uniform(80, 98), 2)
    return np.random.choice(diseases), confidence

uploaded_file = st.file_uploader("📤 Upload Leaf Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Diagnose Disease"):
        processed_image = preprocess_image(image)

        disease, confidence = predict(processed_image)

        st.success(f"🌱 **Disease Detected:** {disease}")
        st.info(f"📊 **Confidence:** {confidence}%")

        # Show processed image for transparency
        st.subheader("🔧 Processed Image Used for Detection")
        st.image((processed_image * 255).astype(np.uint8), use_column_width=True)
