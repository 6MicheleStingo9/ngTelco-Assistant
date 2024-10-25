import streamlit as st
from data.docs import offers_docs
from models.cohere import llm, embeddings
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


neo4jvector = Neo4jVector.from_documents(
    documents=offers_docs,
    embedding=embeddings,
    url=st.secrets["NEO4J_URI"],
    password=st.secrets["NEO4J_PASSWORD"],
    search_type="hybrid",
)


retriever = neo4jvector.as_retriever()

instructions = (
    "Use the given context to answer the question."
    "If you don't know the answer, say you don't know."
    "Context: {context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", instructions),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
chain_retriever = create_retrieval_chain(retriever, question_answer_chain)


def get_vector_info(input):
    return chain_retriever.invoke({"input": input})
