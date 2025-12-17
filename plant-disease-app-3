import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="Plant Disease Detector", layout="centered")

st.title("🌿 Plant Disease Detection (Leaf Only)")
st.write("⚠ Upload only **leaf images**. Other images will be rejected.")

# ---------- LEAF VALIDATION ----------
def is_leaf(image):
    img = np.array(image)
    img = cv2.resize(img, (224, 224))
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    # Green color range (leaf detection)
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([90, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    green_ratio = np.sum(mask > 0) / (224 * 224)

    return green_ratio > 0.15  # Threshold

# ---------- IMAGE PREPROCESSING ----------
def preprocess_image(image):
    img = np.array(image)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    return img

# ---------- DUMMY DISEASE MODEL ----------
def predict(image_array):
    diseases = ["Healthy", "Rust", "Red Rot", "Blight"]
    return np.random.choice(diseases)

uploaded_file = st.file_uploader("📤 Upload Leaf Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Diagnose"):
        if not is_leaf(image):
            st.error("❌ Invalid Image! Please upload a **leaf image only**.")
        else:
            processed = preprocess_image(image)
            result = predict(processed)
            st.success(f"🌱 Disease Detected: **{result}**")
