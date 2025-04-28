import streamlit as st
from langchain_cohere import ChatCohere, CohereEmbeddings

key = st.secrets["COHERE_API_KEY_AD"]


llm = ChatCohere(
    model="command-r-plus-08-2024",
    cohere_api_key=key,
)

embeddings = CohereEmbeddings(
    model="embed-multilingual-v3.0",
    cohere_api_key=key,
)
