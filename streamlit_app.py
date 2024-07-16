import streamlit as st 
from PIL import Image
from rembg import remove 
import io
import os

def process_image(image_uploaded):
    image = Image.open(image_uploaded)
    processed_image = remove_background(image)
    return processed_image

def remove_background(image):
    image_byte = io.BytesIO()
    image.save(image_byte, format="PNG")
    image_byte.seek(0)
    processed_image_bytes = remove(image_byte.read())
    return Image.open(io.BytesIO(processed_image_bytes))

# Asegúrate de que el archivo exista antes de intentar cargarlo
image_path = "assets/camaroremove.JPG"
if os.path.exists(image_path):
    st.image(image_path)
else:
    st.warning(f"La imagen {image_path} no fue encontrada.")

st.header("Aplicación para Eliminar Fondo")
st.subheader("Sube una Imagen")
upload_image = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if upload_image is not None:
    st.image(upload_image, caption="Imagen subida", use_column_width=True)
    remove_button = st.button(label="Quitar Fondo")
    if remove_button:
        processed_image = process_image(upload_image)
        st.image(processed_image, caption="Fondo Eliminado", use_column_width=True)
        processed_image.save("processed_image.png")
        with open("processed_image.png", "rb") as f:
            image_data = f.read()
            st.download_button("Descargar Imagen Procesada", data=image_data, file_name="imagen_procesada.png")
            os.remove("processed_image.png")
