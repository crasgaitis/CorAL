import streamlit as st
import sklearn
import pandas as pd
import numpy as np
import math
from PIL import Image
import pickle
import joblib
import random
# import tensorflow as tf

# loading

with open("model_new.pkl", 'rb') as file:
    clf = pickle.load(file)


#model = tf.keras.models.load_model('model.h5')

st.title('CorAL')

# user input
st.write("Upload neural activity here:")

userdf = st.file_uploader("upload file", type={"csv"})
if userdf is not None:
    userdf = pd.read_csv(userdf)
st.write(userdf)

# get user data
