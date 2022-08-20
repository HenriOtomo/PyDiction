from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title('PyDiction')
st.title('I- Présentation de l application et chargement des données')

st.text("Ce projet de machine learning et de météorologie s'est déroulé dans le cadre de notre formation chez DataScientest.")
st.text("L'outil permet de prédire la présence de pluie à J+1 sur n importe quel point géographique du territoire australien à partir des données climatiques, il  est considéré qu il pleut si la quantité de pluie est strictement supérieure à 1mm")
st.text("chargez d'abord vos données, elles doivent être de la meme forme que ce dataset https://www.kaggle.com/jsphyg/weather-dataset-rattle-package sur lequel a été entrainé notre modèle")        
dataset_uploaded = st.file_uploader('charger les données en cliquant sur Browser')
