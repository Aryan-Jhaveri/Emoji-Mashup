import streamlit as st
from PIL import Image
import io
import requests
from transformers import ViTFeatureExtractor, ViTModel
from diffusers import StableDiffusionPipeline
import torch
import numpy as np
import gc

@st.cache_resource
def load_feature_extractor():
    return ViTFeatureExtractor.from_pretrained("google/vit-base-patch16-224")

@st.cache_resource
def load_vit_model():
    return ViTModel.from_pretrained("google/vit-base-patch16-224", torchscript=True)

@st.cache_resource
def load_sd_model():
    return StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16, revision="fp16")

@st.cache_data
def load_emoji(emoji_code):
    url = f"https://raw.githubusercontent.com/googlefonts/noto-emoji/main/png/128/emoji_u{emoji_code}.png"
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content)).convert('RGB')
    return img

@st.cache_data
def extract_features(image, feature_extractor, vit_model):
    image = image.convert('RGB')
    image_np = np.array(image)
    inputs = feature_extractor(images=image_np, return_tensors="pt")
    with torch.no_grad():
        outputs = vit_model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def generate_mashup(emoji1_features, emoji2_features, sd_model):
    combined_features = (emoji1_features + emoji2_features) / 2
    prompt = "An emoji that combines aspects of both input emojis"
    with torch.no_grad():
        image = sd_model(prompt=prompt, latents=combined_features, num_inference_steps=30).images[0]
    return image

st.title("Emoji Mashup Generator")

emoji1 = st.selectbox("Select first emoji", ["1f600", "1f60e", "1f914"])
emoji2 = st.selectbox("Select second emoji", ["1f355", "1f308", "1f680"])

if st.button("Generate Mashup"):
    with st.spinner("Generating mashup..."):
        try:
            img1 = load_emoji(emoji1)
            img2 = load_emoji(emoji2)

            feature_extractor = load_feature_extractor()
            vit_model = load_vit_model()
            
            features1 = extract_features(img1, feature_extractor, vit_model)
            features2 = extract_features(img2, feature_extractor, vit_model)

            del vit_model
            gc.collect()
            torch.cuda.empty_cache()

            sd_model = load_sd_model()
            mashup = generate_mashup(features1, features2, sd_model)

            del sd_model
            gc.collect()
            torch.cuda.empty_cache()

            st.image(img1, caption="Emoji 1", width=100)
            st.image(img2, caption="Emoji 2", width=100)
            st.image(mashup, caption="Mashup Result", width=200)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

st.text("Note: This is a prototype and results may vary.")
