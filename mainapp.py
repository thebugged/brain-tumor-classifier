import os
import numpy as np
import streamlit as st

from PIL import Image, ImageOps
from sqlalchemy.exc import SQLAlchemyError
from tensorflow.keras.models import model_from_json


st.set_page_config(
    page_title="Brain Tumor Classifier",
    page_icon="🧠",
    initial_sidebar_state="collapsed",
    layout="wide"
)
    
hide_streamlit_style = """
            <style>
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)    


# Load the model
model_path_json = "models/brain_model.json"
model_path_weights = "models/brain_weights.h5"

if not os.path.exists(model_path_json):
    st.error(f"Model JSON file not found at {model_path_json}")
    st.stop()
if not os.path.exists(model_path_weights):
    st.error(f"Model weights file not found at {model_path_weights}")
    st.stop()

with open(model_path_json, "r") as json_file:
    loaded_model_json = json_file.read()

loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(model_path_weights)


def preprocess_image(image_data):
    size = (224, 224 )
    image1 = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
    image1 = image1.convert('RGB')
    img = np.array(image1) / 255.0
    img_reshape = img[np.newaxis, ...]
    return img_reshape

def predict_image(model, img_reshape):
    prediction = model(img_reshape)
    return prediction

def update_dataframe(conn, refresh=False):
    if 'predictions_df' not in st.session_state or refresh:
        try:
            predictions_df = conn.query('SELECT * FROM predictions')
            st.session_state['predictions_df'] = predictions_df
        except SQLAlchemyError as e:
            st.error(f"An error occurred while querying the database: {e}")


# Main
st.header("Brain Tumor Classifier")
st.divider()
st.markdown("")

# Initialize connection and create table if it doesn't exist
conn = st.connection('predictions_db', type='sql')
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS predictions (id INTEGER PRIMARY KEY AUTOINCREMENT, image_name TEXT, prediction TEXT);')
    s.commit()

col1, col2 = st.columns(2)

with col1:
    st.markdown("##### Brain Tumors?")
    with st.expander("**About** ", expanded=True):
        st.write("A brain tumor is a mass or growth of abnormal cells in the brain. Tumors can be either benign (non-cancerous) "
                 "or malignant (cancerous). They can originate in the brain itself or spread from other parts of the body.")

    with st.expander("**Symptoms and Signs**", expanded=True):
        st.write("Common symptoms of brain tumors include headaches, seizures, changes in vision, difficulty speaking or "
                 "understanding speech, and changes in mood or personality.")

    with st.expander("**How to Monitor Brain Health and Seek Help**", expanded=True):
        st.write("1. Regular medical check-ups and screenings can help monitor brain health.\n"
                 "2. Pay attention to any unusual symptoms and seek medical advice if you notice persistent changes.\n"
                 "3. Early detection and treatment are crucial for better outcomes.")
        st.markdown("Get sample images [here](https://www.kaggle.com/datasets/fernando2rad/brain-tumor-mri-images-44c)")
    

with col2:
    st.markdown("")
    file = st.file_uploader("Upload an MRI Scan - Pituitary, Glioma or Meningioma", type=["png", "jpg", "jpeg"])

    labels = ['Pituitary', 'Notumor', 'Glioma', 'Meningioma']

    if file is not None:
        image = Image.open(file)
        img_reshape = preprocess_image(image)
        predictions = predict_image(loaded_model, img_reshape)
        predictions = np.argmax(predictions.numpy())
        predictions = labels[predictions]
        string = "Prediction: " + predictions
        col1, col2 = st.columns(2)
        
        # Save the prediction to the database
        try:
            with conn.session as s:
                s.execute('INSERT INTO predictions (image_name, prediction) VALUES (:image_name, :prediction);',
                          {'image_name': file.name, 'prediction': predictions})
                s.commit()
           
            update_dataframe(conn, refresh=True)
        except SQLAlchemyError as e:
            st.error(f"An error occurred while saving the prediction to the database: {e}")

        with col1:
            st.image(image, use_column_width=True)
        with col2:
            st.success(string)


view_predictions = st.checkbox("View Predictions History")

if view_predictions:
    update_dataframe(conn, refresh=True)
    st.dataframe(st.session_state['predictions_df'])

st.divider()
st.markdown("👨🏾‍💻 by [thebugged](https://github.com/thebugged)")


