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
def extract_features(image, _feature_extractor, _vit_model):
    image = image.convert('RGB')
    image_np = np.array(image)
    inputs = _feature_extractor(images=image_np, return_tensors="pt")
    with torch.no_grad():
        outputs = _vit_model(**inputs)
    
    if isinstance(outputs, tuple):
        features = outputs[0]
    elif isinstance(outputs, torch.Tensor):
        features = outputs
    elif hasattr(outputs, 'last_hidden_state'):
        features = outputs.last_hidden_state
    else:
        raise ValueError(f"Unexpected output format from _vit_model: {type(outputs)}")
    
    return features.mean(dim=1).cpu().numpy()

def generate_mashup(emoji1_features, emoji2_features, sd_model):
    combined_features = (emoji1_features + emoji2_features) / 2
    prompt = "An emoji that combines aspects of both input emojis"
    with torch.no_grad():
        image = sd_model(prompt=prompt, latents=combined_features, num_inference_steps=30).images[0]
    return image

st.title("Emoji Mashup Generator")

emoji1 = st.selectbox("Select first emoji", ["1f600", "1f60e", "1f914"])
emoji2 = st.selectbox("Select second emoji", ["1f355", "1f308", "1f680"])

col1, col2 = st.columns(2)
with col1:
    st.image(load_emoji(emoji1), caption="Emoji 1", width=100)
with col2:
    st.image(load_emoji(emoji2), caption="Emoji 2", width=100)

if st.button("Generate Mashup"):
    progress_bar = st.progress(0)
    with st.spinner("Generating mashup..."):
        try:
            progress_bar.progress(10)
            img1 = load_emoji(emoji1)
            img2 = load_emoji(emoji2)
            progress_bar.progress(30)

            feature_extractor = load_feature_extractor()
            vit_model = load_vit_model()
            
            progress_bar.progress(50)
            try:
                features1 = extract_features(img1, feature_extractor, vit_model)
                features2 = extract_features(img2, feature_extractor, vit_model)
            except ValueError as ve:
                st.error(f"Error during feature extraction: {str(ve)}")
                    return

            del vit_model
            gc.collect()
            torch.cuda.empty_cache()

            progress_bar.progress(70)
            sd_model = load_sd_model()
            mashup = generate_mashup(features1, features2, sd_model)

            del sd_model
            gc.collect()
            torch.cuda.empty_cache()

            progress_bar.progress(100)
            st.image(mashup, caption="Mashup Result", width=200)
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
        finally:
            progress_bar.empty()

st.text("Note: This is a prototype and results may vary.")
