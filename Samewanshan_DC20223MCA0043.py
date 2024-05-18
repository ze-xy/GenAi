import streamlit as st
from PIL import Image, ImageOps
import numpy as np
st.title("Simple Image Processing Dashboard")
uploaded_file = st.file_uploader("Choose a JPEG file", type="jpeg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.write("Original Image:")
    st.image(image, caption='Uploaded Image', use_column_width=True)
    grayscale_image = ImageOps.grayscale(image)
    st.write("Grayscale Image:")
    st.image(grayscale_image, caption='Grayscale Image', use_column_width=True)
else:
    st.write("Please upload a JPEG file.")
