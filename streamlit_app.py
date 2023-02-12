import streamlit as st
import sklearn
import pandas as pd
import numpy as np
import math
from PIL import Image
import pickle
import joblib
import random
import tensorflow as tf

# loading

# full_pipeline = joblib.load('pipeline.joblib')

model = tf.keras.models.load_model('model.h5')

st.title('CorAL')
 

# user input
st.sidebar.subheader("Upload neural activity here:")

userdf = st.file_uploader("upload file", type={"csv"})
if userdf is not None:
    userdf = pd.read_csv(userdf)
st.write(userdf)

# get user data
