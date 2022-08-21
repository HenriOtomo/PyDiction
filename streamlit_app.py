

###cellule d'imports (spécifique au code) (tous regroupés ici pour une lecture allégée du code ensuite )

from collections import namedtuple

import streamlit as st

import altair as alt
import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import model_selection, preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.feature_selection import VarianceThreshold, SelectKBest, SelectFromModel, f_regression, mutual_info_regression, RFE, RFECV
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn import metrics
import statsmodels.api 
import statsmodels.api as sm
from scipy.stats import pearsonr
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import chi2_contingency
from sklearn import model_selection, preprocessing
from sklearn.neighbors import KNeighborsClassifier
!pip install imblearn
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler,  ClusterCentroids
from sklearn.metrics import roc_curve,auc
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
!pip install imblearn
from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.under_sampling import RandomUnderSampler,  ClusterCentroids
from sklearn.decomposition import PCA
from sklearn.metrics import mean_absolute_error as mae

#Code pour la préparation des données et la visualisation :

#introduction pour l'utilisateur et chargement des données
st.title('PyDiction')
st.title("Présentation de l' application et chargement des données :")
st.text("Ce projet de machine learning et de météorologie s'est déroulé dans le cadre de notre formation chez DataScientest.")
st.text("L'outil permet de prédire la présence de pluie à J+1 sur n importe quel point géographique du territoire australien à partir des données climatiques, il  est considéré qu il pleut si la quantité de pluie est strictement supérieure à 1mm")
st.text("chargez d'abord vos données, elles doivent être de la meme forme que ce dataset https://www.kaggle.com/jsphyg/weather-dataset-rattle-package sur lequel a été entrainé notre modèle")        
df = st.file_uploader('charger les données en cliquant sur Browser')

#visualisation des variables pour l'utilisateur et guide pour la sélection des variables
st.text("Voici les variables de votre dataset :")
display(df.columns)
