import requests
import streamlit as st
from neo4j import GraphDatabase
from models.fullname import getFullname


def get_id(driver, nome, cognome):
    records, _, _ = driver.execute_query(
        "MATCH (u:Utente {nome: $nome, cognome: $cognome}) RETURN u.id",
        nome=nome,
        cognome=cognome,
    )
    for record in records:
        id = record["u.id"]
        records
        return id


def fetch_user_movements(input):
    """Fetch user data from endpoint"""
    map = getFullname(input)
    driver = GraphDatabase.driver(
        st.secrets["NEO4J_URI"],
        auth=(
            st.secrets["NEO4J_USERNAME"],
            st.secrets["NEO4J_PASSWORD"],
        ),
    )
    user_id = get_id(driver, map.name, map.surname)
    driver.close()
    url = (
        f"https://66fd6873699369308955173f.mockapi.io/ngtelco/users/{user_id}/movements"
    )
    response = requests.get(url)
    response.raise_for_status()  # Solleva un'eccezione se la richiesta fallisce
    print(response.json())
    return response.json()


def get_mov_list(input):
    print(input)
    return fetch_user_movements(input)
