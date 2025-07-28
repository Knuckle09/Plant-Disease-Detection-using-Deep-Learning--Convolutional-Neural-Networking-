import streamlit as st
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd
import os

# Load data
disease_info = pd.read_csv('disease_info.csv', encoding='cp1252')
supplement_info = pd.read_csv('supplement_info.csv', encoding='cp1252')

# Load model
model = CNN.CNN(39)
model.load_state_dict(torch.load("plant_disease_model_1_latest.pt", map_location=torch.device('cpu')))
model.eval()

# Prediction function
def predict(image):
    image = image.resize((224, 224))
    input_data = TF.to_tensor(image)
    input_data = input_data.view((-1, 3, 224, 224))
    output = model(input_data)
    output = output.detach().numpy()
    index = np.argmax(output)
    return index

# Streamlit UI
st.set_page_config(page_title="🌿 Plant Disease Detection", layout="centered")

st.title("🌿 Plant Disease Detection App")
st.write("Upload a picture of a plant leaf, and the app will detect its disease!")

uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Analyzing...")

    pred = predict(image)

    # Get prediction info
    title = disease_info['disease_name'][pred]
    description = disease_info['description'][pred]
    prevent = disease_info['Possible Steps'][pred]
    image_url = disease_info['image_url'][pred]

    supplement_name = supplement_info['supplement name'][pred]
    supplement_image_url = supplement_info['supplement image'][pred]
    supplement_buy_link = supplement_info['buy link'][pred]

    # Display results
    st.subheader(f"🦠 Disease: {title}")
    st.image(image_url, caption="Reference Disease Image", use_column_width=True)
    st.write("📄 **Description:**", description)
    st.write("🛡️ **Prevention Steps:**", prevent)

    st.markdown("---")
    st.subheader("🧪 Recommended Supplement")
    st.image(supplement_image_url, width=200, caption=supplement_name)
    st.markdown(f"[🛒 Buy Now]({supplement_buy_link})")

