import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Configuración visual de la página
st.set_page_config(page_title="Sommelier AI", page_icon="🍷")

# 1. Cargar claves secretas
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

st.title("🍷 Sommelier AI")
st.markdown("Tu experto en vinos personal (RAG + Llama 3)")

# 2. Función para cargar el cerebro (con caché para que sea rápido)
@st.cache_resource
def cargar_cerebro():
    # Ruta a la carpeta que descargaste y renombraste
    persist_directory = "./chroma_db_data"
    
    if not os.path.exists(persist_directory):
        st.error(f"❌ Error: No encuentro la carpeta '{persist_directory}'. ¿La moviste aquí?")
        return None

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    return db

# Cargamos la DB
vector_db = cargar_cerebro()

# 3. Chat
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for msg in st.session_state.mensajes:
    with st.chat_message(msg["rol"]):
        st.markdown(msg["contenido"])

if prompt := st.chat_input("Ej: Busco un vino tinto dulce para postre"):
    st.session_state.mensajes.append({"rol": "user", "contenido": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if vector_db:
            # A. Búsqueda
            docs = vector_db.similarity_search(prompt, k=3)
            contexto = "\n".join([d.page_content for d in docs])
            
            # B. Generación
            llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5, groq_api_key=groq_api_key)
            template = """
            Eres un sommelier experto. Responde en español.
            Usa SOLO este contexto (reseñas en inglés) para recomendar:
            {context}
            
            Usuario: {question}
            """
            prompt_template = ChatPromptTemplate.from_template(template)
            chain = prompt_template | llm
            
            respuesta = chain.invoke({"context": contexto, "question": prompt})
            
            st.markdown(respuesta.content)
            st.session_state.mensajes.append({"rol": "assistant", "contenido": respuesta.content})