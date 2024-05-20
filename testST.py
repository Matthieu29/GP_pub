import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Titre de l'application
st.title("Carte de Montpellier avec des informations détaillées")

# Chemin des fichiers .ods (remplace par les chemins réels)
panneau_pub_file = 'panneau_pub.ods'
type_panneau_file = 'type_panneau.ods'

# Lire les fichiers .ods
df_panneau_pub = pd.read_excel(panneau_pub_file, engine='odf')
df_type_panneau = pd.read_excel(type_panneau_file, engine='odf')

# Vérifier les premières lignes des dataframes pour s'assurer de la bonne lecture
st.write("Aperçu des données des panneaux :", df_panneau_pub.head())
st.write("Aperçu des types de panneaux :", df_type_panneau.head())

# Fusionner les données en utilisant la colonne 'type'
df = pd.merge(df_panneau_pub, df_type_panneau, on='type de panneau')

# Créer une carte centrée sur Montpellier
montpellier_coords = [43.6119, 3.8772]
m = folium.Map(location=montpellier_coords, zoom_start=13)

# Ajouter des points rouges avec des popups détaillés
for index, row in df.iterrows():
    popup_text = f"""
    <b>Nom:</b> {row['id']}<br>
    <b>Consommation:</b> {row['consommation']}
    """
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,  # Taille du point
        color='red',  # Couleur du bord
        fill=True,
        fill_color='red',  # Couleur de remplissage
        fill_opacity=0.7,  # Opacité
        popup=popup_text
    ).add_to(m)

# Afficher la carte dans Streamlit
st_folium(m, width=700, height=500)
