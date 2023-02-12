import streamlit as st
import sklearn
import pandas as pd
import numpy as np
import math
from PIL import Image
import pickle
import joblib
import random
import re
import pyfirmata
import serial
import time
# import tensorflow as tf

# [BAD] board = pyfirmata.Arduino('COM5')
# arduino = serial.Serial(port = "COM5", timeout=0)

st.markdown(
     f"""
     <style>
     
    .stApp {{
            background: url("https://i.imgur.com/yF9sYx6.jpg");
            background-size: cover
        }}

 
     </style>
     """,
     unsafe_allow_html=True
 )

# loading

with open("model_new.pkl", 'rb') as file:
    clf = pickle.load(file)


#model = tf.keras.models.load_model('model.h5')

image = Image.open('logo.JPG')
st.image(image)

# user input
st.write("Upload neural activity here:")

try:
    userdf = st.file_uploader("upload file", type={"csv"})
    if userdf is not None:
        userdf = pd.read_csv(userdf)
    st.write('Raw data:')
    st.write(userdf)

    def consolidate(freq_min, freq_max, brainwave):
        pattern = re.compile(rf".*[{freq_min}-{freq_max}]Hz.*")
        columns_to_include = [col for col in userdf.columns if re.match(pattern, col)]

        bw_average = userdf[columns_to_include].mean(axis=1)
        bw_median = np.array([np.median(bw_average)])

        # take delta average across all channels, and median of this average across timestamps
        df_temp[f"{brainwave}"] = bw_median


    while True:
        df_temp = pd.DataFrame()
        df = pd.DataFrame()

        pattern = re.compile("^Aux|^f_")
        unwanted = [col for col in userdf.columns if re.match(pattern, col)]
        userdf = userdf.drop(columns=unwanted)
        userdf = userdf.drop('info', axis=1)

        consolidate(1, 3, "Delta")
        consolidate(4, 7, "Theta")
        consolidate(8, 9, "Alpha1")
        consolidate(10, 11, "Alpha2")
        consolidate(12, 20, "Beta1")
        consolidate(20, 29, "Beta2")
        
        st.write('Converted values:')
        st.write(df_temp)

        pred = clf.predict(df_temp)[0]
        # [KINDA BAD] st.write(pred)
        # arduino.write(str.encode(pred))
        if pred == 0:
            st.write('Student understands material!')
            
        else:
            st.write('Student is confused.')
            # [BAD] board.digital[13].write(1)


except:
    pass