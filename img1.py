import streamlit as st
from PIL import Image,ImageFilter
import io


def convert_image(image, format):
    image_convert = image.convert("RGB")
    image_bytes = io.BytesIO()
    image_convert.save(image_bytes, format = format)
    return image_bytes.getvalue()

def buat_filter(image, jenis_filter):
    if jenis_filter == "BLUR":
        gambar_filter = image.filter(ImageFilter.BLUR)
    elif jenis_filter == "CONTOUR":
        gambar_filter = image.filter(ImageFilter.CONTOUR)
    elif jenis_filter == "SMOOTH":
        gambar_filter = image.filter(ImageFilter.SMOOTH)
    elif jenis_filter == "EMBOSS":
        gambar_filter = image.filter(ImageFilter.EMBOSS)
    elif jenis_filter == "FIND_EDGES":
        gambar_filter = image.filter(ImageFilter.FIND_EDGES)
    else:
        gambar_filter = image.filter(ImageFilter.SHARPEN)
    return gambar_filter

def page_7():
    unggah_gambar = st.file_uploader('Choose Image:', type=["JPG","JPEG","PNG"])
    if unggah_gambar is not None:
        gambar = Image.open(unggah_gambar)
        col1, col2, col3 = st.columns(3)
        pilih_filter = col2.selectbox("Pilih Jenis Filter",["BLUR","CONTOUR", "SMOOTH", "EMBOSS", "FIND_EDGES", "SHARPEN"])
        
        col1.image(gambar, caption="Original", width=200)   
        filtered_image = buat_filter(gambar, pilih_filter.upper())
        col3.image(filtered_image, caption="Filtered Result",width=200)  
        image_bytes = convert_image(filtered_image,"PNG")
        col2.download_button(label="Download Here!", data = image_bytes, file_name ="Result.png")