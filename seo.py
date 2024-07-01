import requests
from bs4 import BeautifulSoup
import streamlit as st

# Función para scrapear datos de una página web
def get_page_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Asegurarse de que la solicitud fue exitosa
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer título de la página
        title = soup.title.string if soup.title else 'No title'
        
        # Extraer meta descripción
        meta_description = ''
        if soup.find("meta", attrs={"name": "description"}):
            meta_description = soup.find("meta", attrs={"name": "description"})['content']
        
        # Extraer meta keywords
        meta_keywords = ''
        if soup.find("meta", attrs={"name": "keywords"}):
            meta_keywords = soup.find("meta", attrs={"name": "keywords"})['content']
        
        return {
            "url": url, 
            "title": title, 
            "meta_description": meta_description,
            "meta_keywords": meta_keywords
        }
    except requests.RequestException as e:
        st.error(f"Error al intentar acceder a la URL: {e}")
        return None

# Interfaz de Streamlit
st.title("SEO Scraper")

# Sección de scraping de datos
st.header("Scraping de Datos Web")
url = st.text_input("Ingrese la URL para scrapear:", "https://www.example.com")
if url:
    data = get_page_data(url)
    if data:
        st.write("**Título de la página:**")
        st.write(data["title"])
        st.write("**Meta descripción:**")
        st.write(data["meta_description"])
        st.write("**Palabras clave (meta keywords):**")
        st.write(data["meta_keywords"])
