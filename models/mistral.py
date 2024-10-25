import streamlit as st
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_mistralai.embeddings import MistralAIEmbeddings

key = st.secrets["MISTRAL_API_KEY"]

llm = ChatMistralAI(
    model="open-mistral-7b",
    api_key=key,
)

embeddings = MistralAIEmbeddings(
    model="mistral-embed",
    api_key=key,
)
