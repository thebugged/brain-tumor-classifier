import sqlite3
import numpy as np
# import pandas as pd
import streamlit as st
import tensorflow as tf

from sqlite3 import Connection
from PIL import Image, ImageOps

st.set_page_config(
    page_title="Brain Tumour Classifier",
    page_icon="🧠",
    # layout="wide",
    initial_sidebar_state="auto",
)

URI_SQLITE_DB = "predictions.db"

def init_db(conn: Connection):
    conn.execute('CREATE TABLE IF NOT EXISTS userstable(PREDICTION TEXT)')
    conn.commit()

def app():
    interpreter = tf.lite.Interpreter(model_path='brain.tflite')
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    print(output_details)

    st.subheader("Brain Tumor Classifier", divider='grey')
    st.markdown("")
    st.caption("Upload an image to determine the type of tumor")

    with st.sidebar:
        st.header("Brain Tumors?")

        with st.expander("About "):
            st.write("A brain tumor is a mass or growth of abnormal cells in the brain. Tumors can be either benign (non-cancerous) "
                    "or malignant (cancerous). They can originate in the brain itself or spread from other parts of the body.")

        with st.expander("Symptoms and Signs "):
            st.write("Common symptoms of brain tumors include headaches, seizures, changes in vision, difficulty speaking or "
                    "understanding speech, and changes in mood or personality.")

        with st.expander("How to Monitor Brain Health and Seek Help"):
            st.write("1. Regular medical check-ups and screenings can help monitor brain health.\n"
                    "2. Pay attention to any unusual symptoms and seek medical advice if you notice persistent changes.\n"
                    "3. Early detection and treatment are crucial for better outcomes.")


    file = st.file_uploader("Please upload your MRI Scan", type=["png", "jpg", "jpeg"])

    conn = get_connection(URI_SQLITE_DB)
    init_db(conn)

    def import_and_predict(image_data):
        size = (256, 256)
        image1 = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
        image1 = image1.convert('RGB')
        img = np.array(image1) / 255.0
        img_reshape = img[np.newaxis, ...]

        # Prepare input data for TensorFlow Lite model
        interpreter.set_tensor(input_details[0]['index'], img_reshape.astype(np.float32))
        interpreter.invoke()

        # Get the output from TensorFlow Lite model
        prediction = interpreter.get_tensor(output_details[0]['index'])

        return prediction

    labels = ['pituitary', 'notumor', 'glioma', 'meningioma']


    if file is not None:
        image = Image.open(file)
        st.image(image, width=300)
        predictions = import_and_predict(image)
        predictions = np.argmax(predictions)
        predictions = labels[predictions]
        string = "The patient most likely has " + predictions
        st.success(string)

@st.cache_resource
def get_connection(path: str):
    return sqlite3.connect(path, check_same_thread=False)

if __name__ == '__main__':
    app()
