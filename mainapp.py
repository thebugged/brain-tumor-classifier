import sqlite3
import numpy as np
import pandas as pd
import streamlit as st

from sqlite3 import Connection
from PIL import Image, ImageOps
from keras.models import load_model

URI_SQLITE_DB = "predictions.db"

st.set_page_config(page_title="BTC", page_icon="favicon.png")

def init_db(conn: Connection):
    conn.execute('CREATE TABLE IF NOT EXISTS userstable(PREDICTION TEXT)')
    conn.commit()
    

def build_sidebar():
    st.sidebar.markdown("### Function")
    st.sidebar.markdown("Brain Tumor Classifier is a web application that processes MRI scans to determine the type of tumor present (Glioma, Meningioma, Pituitary) or if there is no tumor present.")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### How to Use")
    st.sidebar.markdown("1. Upload an MRI scan (in PNG, JPG, or JPEG format).")
    st.sidebar.markdown("2. The application will analyze the scan and provide the predicted tumor type or indicate no tumor.")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Output")
    st.sidebar.markdown("The application will display the predicted tumor type or indicate no tumor.")

def app():
    model = load_model('resnet.h5')

    st.title("Brain Tumor Classifier")
    st.markdown("")
    st.markdown("")

    st.markdown("<h4 style='text-align: center;'>Upload the MRI Scan and get Result</h4>", unsafe_allow_html=True)

    file = st.file_uploader("Please upload your MRI Scan", type=["png", "jpg", "jpeg"])

    conn = get_connection(URI_SQLITE_DB)
    build_sidebar()
    init_db(conn)

    def import_and_predict(image_data):
        size = (256, 256)
        image1 = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image1 = image1.convert('RGB')
        img = np.array(image1) / 255.0
        img_reshape = img[np.newaxis, ...]
        img_reshape = img.reshape(1, 256, 256, 3)
        prediction = model.predict(img_reshape)
        return prediction

    labels = ['pituitary', 'notumor', 'glioma', 'meningioma']

    if file is None:
        st.markdown("<h5 style='text-align: center;'>Please Upload a File</h5>", unsafe_allow_html=True)
    else:
        image = Image.open(file)
        st.image(image, width=300)
        predictions = import_and_predict(image)
        predictions = np.argmax(predictions)
        predictions = labels[predictions]
        string = "The patient most likely has " + predictions
        st.success(string)

    st.sidebar.markdown("", unsafe_allow_html=True)
    st.sidebar.markdown("", unsafe_allow_html=True)
    st.sidebar.markdown("", unsafe_allow_html=True)
    st.sidebar.markdown("", unsafe_allow_html=True)


@st.cache_resource
def get_connection(path: str):
    return sqlite3.connect(path, check_same_thread=False)


if __name__ == '__main__':
    app()
