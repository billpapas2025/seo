import requests
import re
import streamlit as st

# Función para scrapear datos de una página web sin BeautifulSoup
def get_page_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Asegurarse de que la solicitud fue exitosa
        
        html = response.text
        
        # Extraer título de la página
        title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        title = title_match.group(1) if title_match else 'No title'
        
        # Extraer meta descripción
        meta_description_match = re.search(r'<meta name="description" content="(.*?)"', html, re.IGNORECASE)
        meta_description = meta_description_match.group(1) if meta_description_match else 'No description'
        
        # Extraer meta keywords
        meta_keywords_match = re.search(r'<meta name="keywords" content="(.*?)"', html, re.IGNORECASE)
        meta_keywords = meta_keywords_match.group(1) if meta_keywords_match else 'No keywords'
        
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
        st.subheader("Resultados del Scraping")
        st.write("**Título de la página:**")
        st.write(data["title"])
        st.write("**Meta descripción:**")
        st.write(data["meta_description"])
        st.write("**Palabras clave (meta keywords):**")
        st.write(data["meta_keywords"])
