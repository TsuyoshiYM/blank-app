import streamlit as st 
from PIL import Image
from rembg import remove 
import io
import os


def process_image(image_uploaded):
    image = Image.open(image_uploaded)
    proccesed_image = remove_background(image)
    
    return proccesed_image

def remove_background(image):
    image_byte = io.BytesIO()
    image.save(image_byte, format="PNG")
    image_byte.seek(0)
    proccesed_image_bytes = remove(image_byte.read())
    
    return Image.open(io.BytesIO(proccesed_image_bytes))

st.image("assets/camaroremove.JPG")
st.header("Background Removal App")
st.subheader("Upload an Image")
upload_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if upload_image is not None:
    st.image(upload_image, caption="Imagen subida", use_column_width=True)
    remove_button = st.button(label="Quitar fondo")
    if remove_button:
        proccesed_image = process_image(upload_image)
        st.image(proccesed_image, caption="Background Removed", use_column_width=True)
        proccesed_image.save("processed_image.png")
        with open("processed_image.png", "rb") as f:
            image_data = f.read()
            st.download_button("Download Processed Image", data=image_data, file_name="processed_image.png")
            os.remove("processed_image.png")
