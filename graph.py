import streamlit as st
from langchain_community.graphs import Neo4jGraph
from neo4j import GraphDatabase
from data.docs import query

graph = Neo4jGraph(
    url=st.secrets["NEO4J_URI"],
    username=st.secrets["NEO4J_USERNAME"],
    password=st.secrets["NEO4J_PASSWORD"],
    enhanced_schema=True,
)


def create_db():
    driver = GraphDatabase.driver(
        st.secrets["NEO4J_URI"],
        auth=(
            st.secrets["NEO4J_USERNAME"],
            st.secrets["NEO4J_PASSWORD"],
        ),
    )

    erase = driver.execute_query(
        "MATCH (n) DETACH DELETE n",
        database_="neo4j",
    ).summary

    print(
        "Erased {nodes_erased} nodes in {time} ms.".format(
            nodes_erased=erase.counters.nodes_deleted,
            time=erase.result_available_after,
        )
    )

    create = driver.execute_query(
        query,
        database_="neo4j",
    ).summary

    print(
        "Created {nodes_created} nodes in {time} ms.".format(
            nodes_created=create.counters.nodes_created,
            time=create.result_available_after,
        )
    )

    driver.close()


def erase_sessions():
    driver = GraphDatabase.driver(
        st.secrets["NEO4J_URI"],
        auth=(
            st.secrets["NEO4J_USERNAME"],
            st.secrets["NEO4J_PASSWORD"],
        ),
    )

    erase = driver.execute_query(
        "MATCH (s:Session) DETACH DELETE s",
        database_="neo4j",
    ).summary

    print(
        "Erased {nodes_erased} nodes in {time} ms.".format(
            nodes_erased=erase.counters.nodes_deleted,
            time=erase.result_available_after,
        )
    )
    driver.close()


def erase_messages():
    driver = GraphDatabase.driver(
        st.secrets["NEO4J_URI"],
        auth=(
            st.secrets["NEO4J_USERNAME"],
            st.secrets["NEO4J_PASSWORD"],
        ),
    )

    erase = driver.execute_query(
        "MATCH (m:Message) DETACH DELETE m",
        database_="neo4j",
    ).summary

    print(
        "Erased {nodes_erased} nodes in {time} ms.".format(
            nodes_erased=erase.counters.nodes_deleted,
            time=erase.result_available_after,
        )
    )
    driver.close()


# print(graph.get_schema)
