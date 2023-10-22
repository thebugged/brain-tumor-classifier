
import sqlite3
import numpy as np
import pandas as pd
import streamlit as st

from sqlite3 import Connection
from PIL import Image ,ImageOps
from keras.models import load_model

URI_SQLITE_DB = "predictions.db"

def init_db(conn: Connection):
    conn.execute ('CREATE TABLE IF NOT EXISTS userstable(NAME TEXT,PREDICTION TEXT)')
    conn.commit()

def build_sidebar(conn: Connection):
    
    st.sidebar.markdown("")
   
    st.sidebar.header("Record Data")

    name = st.sidebar.text_input ("Name")
    prediction = st.sidebar.text_input("Prediction")

    if st.sidebar.button("Save to database"):
        conn.execute('INSERT INTO userstable(NAME,PREDICTION) VALUES (?,?)',(name,prediction))
        st.sidebar.success("Data saved to database")
        conn.commit()

def get_data(conn: Connection):
    df = pd.read_sql("SELECT * FROM userstable", con=conn)
    return df

def display_data(conn: Connection):
    if st.sidebar.checkbox("Display data in sqlite databse"):
        st.sidebar.dataframe(get_data(conn))

def app():
  model = load_model('mobilenet.h5')
  st.success("MobileNetV2 Model Loaded")

  st.markdown("", unsafe_allow_html=True)
  st.markdown("", unsafe_allow_html=True)

  st.markdown("<h4 style='text-align: center;'>Upload the MRI Scan and get Result</h4>", unsafe_allow_html=True)


  file = st.file_uploader("Please upload your MRI Scan",type = ["png","jpg","jpeg"] )
  
  conn = get_connection(URI_SQLITE_DB)
  build_sidebar(conn)
  init_db(conn)
  display_data(conn)

  def import_and_predict(image_data): 
      size= (256,256)
      image1 = ImageOps.fit(image_data,size,Image.ANTIALIAS)
      image1 = image1.convert('RGB')
      img = np.array(image1)/255.0
      img_reshape = img[np.newaxis,...]
      img_reshape = img.reshape(1,256,256,3)
      prediction = model.predict(img_reshape)
      return prediction

  
  labels = ['glioma', 'meningioma', 'notumor', 'pituitary']
    
  if file is None:
   
    st.markdown("<h5 style='text-align: center;'>Please Upload a File</h5>", unsafe_allow_html=True)
  else:
    
    image = Image.open(file)
    st.image(image, width=300)
    predictions = import_and_predict(image)
    predictions = np.argmax(predictions)
    predictions = labels[predictions]
    string = "The patient most likely has "+ predictions
    st.success(string)


  st.sidebar.markdown("", unsafe_allow_html=True)
  st.sidebar.markdown("", unsafe_allow_html=True)
  st.sidebar.markdown("", unsafe_allow_html=True)
  st.sidebar.markdown("", unsafe_allow_html=True)
  


@st.cache(hash_funcs={Connection: id})
def get_connection(path: str):
    
    return sqlite3.connect(path, check_same_thread=False)  
 
                 


  