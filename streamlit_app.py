

###cellule d'imports (spécifique au code) (tous regroupés ici pour une lecture allégée du code ensuite )

from collections import namedtuple
import streamlit as st
import altair as alt
import math
import pandas as pd

#Code pour la préparation des données et la visualisation :

#introduction pour l'utilisateur et chargement des données
st.title('PyDiction')
st.title("Présentation de l' application et chargement des données :")
st.text("Ce projet de machine learning et de météorologie s'est déroulé dans le cadre de notre formation chez DataScientest.")
st.text("L'outil permet de prédire la présence de pluie à J+1 sur n importe quel point géographique du territoire australien à partir des données climatiques, il  est considéré qu il pleut si la quantité de pluie est strictement supérieure à 1mm")
st.text("chargez d'abord vos données, elles doivent être de la meme forme que ce dataset https://www.kaggle.com/jsphyg/weather-dataset-rattle-package sur lequel a été entrainé notre modèle")        
df = st.file_uploader('charger les données en cliquant sur Browser')

