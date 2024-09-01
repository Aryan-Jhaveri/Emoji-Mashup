import streamlit as st
from PIL import Image
import io
import requests
from transformers import ViTFeatureExtractor, ViTModel
from diffusers import StableDiffusionPipeline
import torch
import numpy as np

@st.cache_resource
def load_models():
    feature_extractor = ViTFeatureExtractor.from_pretrained("google/vit-base-patch16-224")
    vit_model = ViTModel.from_pretrained("google/vit-base-patch16-224")
    sd_model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float32)
    return feature_extractor, vit_model, sd_model

feature_extractor, vit_model, sd_model = load_models()

def load_emoji(emoji_code):
    url = f"https://raw.githubusercontent.com/googlefonts/noto-emoji/main/png/128/emoji_u{emoji_code}.png"
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content)).convert('RGB')
    return img

def extract_features(image):
    # Ensure image is in RGB format
    image = image.convert('RGB')
    # Convert image to numpy array
    image_np = np.array(image)
    inputs = feature_extractor(images=image_np, return_tensors="pt")
    outputs = vit_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def generate_mashup(emoji1_features, emoji2_features):
    combined_features = (emoji1_features + emoji2_features) / 2
    prompt = "An emoji that combines aspects of both input emojis"
    image = sd_model(prompt=prompt, latents=combined_features).images[0]
    return image

st.title("Emoji Mashup Generator")

emoji1 = st.selectbox("Select first emoji", ["1f600", "1f60e", "1f914"])
emoji2 = st.selectbox("Select second emoji", ["1f355", "1f308", "1f680"])

if st.button("Generate Mashup"):
    with st.spinner("Generating mashup..."):
        try:
            img1 = load_emoji(emoji1)
            img2 = load_emoji(emoji2)
            features1 = extract_features(img1)
            features2 = extract_features(img2)
            mashup = generate_mashup(features1, features2)
            
            st.image(img1, caption="Emoji 1", width=100)
            st.image(img2, caption="Emoji 2", width=100)
            st.image(mashup, caption="Mashup Result", width=200)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

st.text("Note: This is a prototype and results may vary.")
