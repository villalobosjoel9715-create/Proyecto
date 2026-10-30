
import streamlit as st

# Configuración de la página principal.
st.set_page_config(
    page_title="EcoGuard AI",
    page_icon="🌍",
    layout="wide"
)

# Presentación de nuestra aplicación.
st.title("🌍 EcoGuard AI")

st.subheader(
    "Inteligencia artificial contra el cambio climático"
)

st.write(
    "Bienvenido a EcoGuard AI, una herramienta para "
    "analizar el medioambiente mediante tecnología."
)

st.divider()

# Primera sección de nuestra aplicación.
st.header("Panel medioambiental")

st.write(
    "Desde aquí podremos consultar información "
    "sobre nuestro planeta."
)

st.success("EcoGuard AI está iniciado correctamente.")
