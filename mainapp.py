import os
import numpy as np
import streamlit as st

from sqlalchemy import text 
from PIL import Image, ImageOps
from sqlalchemy.exc import SQLAlchemyError
from tensorflow.keras.models import model_from_json


st.set_page_config(
    page_title="Brain Tumor Classifier",
    page_icon="🧠",
    initial_sidebar_state="collapsed",
    layout="wide"
)


# Load model
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


# Helpers
def preprocess_image(image_data):
    size = (224, 224)
    image1 = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
    image1 = image1.convert('RGB')
    img = np.array(image1) / 255.0
    img_reshape = img[np.newaxis, ...]
    return img_reshape

def predict_image(model, img_reshape):
    prediction = model(img_reshape)
    return prediction

def update_dataframe(conn):
    try:
        predictions_df = conn.query('SELECT * FROM predictions ORDER BY id DESC')
        return predictions_df
    except SQLAlchemyError as e:
        st.error(f"An error occurred while querying the database: {e}")
        return None

def clear_history(conn):
    try:
        with conn.session as s:
            s.execute(text('DELETE FROM predictions'))
            s.commit()
        return True
    except SQLAlchemyError as e:
        st.error(f"An error occurred while clearing history: {e}")
        return False


# DB init
conn = st.connection('predictions_db', type='sql')
with conn.session as s:
    s.execute(text(
        'CREATE TABLE IF NOT EXISTS predictions ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'image_name TEXT, '
        'prediction TEXT'
        ');'
    ))
    s.commit()


st.header("Brain Tumor Classifier")

tab1, tab2 = st.tabs(["Overview", "Classify"])

# Overview tab
with tab1:
    st.markdown("**What is a Brain Tumor?**")
    st.markdown("""
        A brain tumor is a mass or growth of abnormal cells in the brain. Tumors can be benign (non-cancerous) 
        or malignant (cancerous). They can originate in the brain or spread from other parts of the body. 
        Common symptoms include headaches, seizures, changes in vision, difficulty speaking, and changes in mood or personality. 
        Early detection and treatment can improve outcomes.
                """
    )
    st.markdown("**Main Types**")
    st.markdown("""
                The types of tumors this application can detect range from the following. 
                Just by looking at them with the human eye, you can't exactly tell which is which.
                """)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.image("images/pituitary/Te-pi_0010.jpg", caption="Pituitary", use_container_width=True)
    with c2:
        st.image("images/glioma/Te-gl_0010.jpg", caption="Glioma", use_container_width=True)
    with c3:
        st.image("images/meningioma/Te-me_0010.jpg", caption="Meningioma", use_container_width=True)
    with c4:
        st.image("images/no tumor/Te-no_0010.jpg", caption="No Tumor", use_container_width=True)

    st.markdown("""
                1. **Pituitary** – Often located at the base of the brain; may affect hormone production and vision.
                2. **Glioma** – Arises from glial cells; can be aggressive and affect various brain functions depending on location.
                3. **Meningioma** – Develops from the membranes surrounding the brain; usually slow-growing and often benign.
                4. **No Tumor** – MRI shows no signs of abnormal growth.
                """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("")
        st.markdown("**Symptoms and Signs**")
        st.markdown("""
        - Persistent headaches  
        - Seizures  
        - Changes in vision  
        - Difficulty speaking or understanding speech  
        - Personality or mood changes  
        - Loss of balance or coordination  
        """)

    with col2:
        st.markdown("")
        st.markdown("**How to Monitor Brain Health**")
        st.markdown("""
        1. Schedule regular medical check-ups and screenings.  
        2. Pay attention to unusual or persistent symptoms.  
        3. Seek medical advice promptly for any concerning changes.  
        4. Follow your doctor's recommendations for imaging or lab tests.  
        """)

# Classify tab
with tab2:
    col1, col2 = st.columns([1, 2])
    
    labels = ['Pituitary', 'Notumor', 'Glioma', 'Meningioma']

    # Upload
    with col1:
        st.markdown("**Upload MRI**")

        file = st.file_uploader(
            "Choose an MRI scan file",
            type=["png", "jpg", "jpeg"],
            key="mri_uploader"
        )

        st.markdown("")
        st.markdown("Get sample images [here](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)")

        
    with col2:
        if file is not None:
            st.markdown("**Results**")
            
            # process the image
            image = Image.open(file)
            img_reshape = preprocess_image(image)
            predictions = predict_image(loaded_model, img_reshape)
            pred_idx = int(np.argmax(predictions.numpy()))
            pred_label = labels[pred_idx]
            
            # create two sub-columns for image and prediction details
            img_col, pred_col = st.columns([1, 1])
            
            # display image
            with img_col:
                st.image(image, use_container_width=True, caption=file.name)
            
            # display prediction details
            with pred_col:
            
                for i, label in enumerate(labels):
                    confidence = float(predictions.numpy()[0][i]) * 100
                    # highlight the predicted class
                    if i == pred_idx:
                        st.markdown(f"**→ {label}: {confidence:.2f}%**")
                        st.progress(confidence / 100)
                    else:
                        st.markdown(f"&nbsp;&nbsp;&nbsp;{label}: {confidence:.2f}%")
                        st.progress(confidence / 100)
                
                if pred_label != 'Notumor':
                    st.markdown("")
                    st.caption("⚠️ Please consult with a medical professional for proper diagnosis.")
                

                st.markdown("")  
                if st.button("🔄 Clear", key="clear_analysis"):
                    if 'mri_uploader' in st.session_state:
                        del st.session_state['mri_uploader']
                    if 'last_saved' in st.session_state:
                        del st.session_state['last_saved']
                    st.rerun()
            
            # save to DB only if not already saved
            save_key = f"{file.name}_{pred_label}"
            if 'last_saved' not in st.session_state or st.session_state.last_saved != save_key:
                try:
                    with conn.session as s:
                        s.execute(
                            text('INSERT INTO predictions (image_name, prediction) VALUES (:image_name, :prediction);'),
                            {'image_name': file.name, 'prediction': pred_label}
                        )
                        s.commit()
                    st.session_state.last_saved = save_key
                    st.session_state.refresh_history = True
                    
                except SQLAlchemyError as e:
                    st.error(f"An error occurred while saving the prediction: {e}")
        else:
            # placeholder when no image is uploaded
            st.markdown("**Results**")
            st.info("← Please upload an MRI scan to see analysis results here")
        
            st.markdown("""
            **How to use:**
            1. Upload an MRI scan image using the file uploader on the left
            2. The AI model will analyze the image and detect if there's a tumor
            3. View confidence scores for each tumor type
            4. Results are automatically saved
            """)