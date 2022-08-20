from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title('PyDiction')
st.title('I- Contexte et Objectifs')

st.text("Ce projet de machine learning et de météorologie s'est déroulé dans le cadre de notre formation chez DataScientest.")
st.text("L'outil permet de prédire la présence de pluie (il  est considéré 'il pleut' si la quantité de pluie est strictement supérieure à 1mm), sur n’importe quel point géographique du territoire australien à partir des données précédemment citées')
dataset_uploaded = st.file_uploader('charger les données ')
