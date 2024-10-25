from models.cohere import llm
from graph import graph
from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain
from langchain_core.prompts import PromptTemplate

CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions and requests into Cypher.
Convert the user's question and requests based on the schema.
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
Be accurate and check for properties within nodes and relationships


Schema:
{schema}

Examples: Here are a few examples of generated Cypher statements for particular questions:

# Recupera i miei contratti
MATCH (u:Utente {{nome:"sofia", cognome:"blu"}})-[r:HA_SOTTOSCRITTO]-(c:Contratto)
RETURN c.file

# Quanti minuti mi rimangono?
MATCH (u:Utente {{nome:"mario", cognome:"rossi"}})-[r:HA_ATTIVATO]-(o:Offerta)
RETURN r.residuoMinuti, o.nome

# Quanti giga mi rimangono?
MATCH (u:Utente {{nome:"luca", cognome:"verdi"}})-[r:HA_ATTIVATO]-(o:Offerta)
RETURN r.residuoDati, o.nome

# Quanti messaggi mi rimangono?
MATCH (u:Utente {{nome:"francesca", cognome:"gialli"}})-[r:HA_ATTIVATO]-(o:Offerta)
RETURN r.residuoSMS, o.nome

# Quali sono le offerte attive?
MATCH (u:Utente {{nome:"mario", cognome:"rossi"}})-[r:HA_ATTIVATO]-(o:Offerta)
RETURN o.nome 

Qual è l'utenza mobile associata al mio account?
MATCH (u:Utente {{nome: 'mario', cognome: 'rossi'}})
RETURN u.utenzaMobile

Quando scade la mia offerta?
MATCH (u:Utente {{nome: 'mario', cognome: 'rossi'}})-[r:HA_ATTIVATO]-(o:Offerta)
RETURN r.dataFine, o.nome

Qual è il costo mensile della mia attuale offerta?
MATCH (u:Utente {{nome: 'mario', cognome: 'rossi'}})-[r:HA_ATTIVATO]->(o:Offerta)
RETURN o.costoMensile

Puoi aiutarmi a ricordare cosa comprende la mia offerta?
MATCH (u:Utente {{nome: 'mario', cognome: 'rossi'}})-[r:HA_ATTIVATO]->(o:Offerta)
RETURN o.descrizione, o.nome

Fine tuning:
Always assign aliases to relationships
Convert string values to lowercase before generating any query


Question:
{question}

Cypher Query:
"""


CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"],
    template=CYPHER_GENERATION_TEMPLATE,
)


CYPHER_QA_TEMPLATE = """You are a friendly and helpful virtual assistant that provides clear and understandable answers.
The information part contains the provided data that you must use to construct a response.
The provided information is authoritative, and you should never doubt it or try to use your internal knowledge to correct it.
Make the answer sound like a friendly and helpful response to the question, without mentioning that you based it on the given information.
If the provided information is empty, kindly say that you don't know the answer.
Ensure the final answer is conversational, easy to read, and reflects a positive and approachable tone.
 Information:
 {context}

 Question: {question}
 Helpful Answer:"""

CYPHER_QA_PROMPT = PromptTemplate(
    input_variables=["context", "question"], template=CYPHER_QA_TEMPLATE
)


cypher_qa = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    verbose=True,
    return_intermediate_steps=False,
    cypher_prompt=CYPHER_GENERATION_PROMPT,
    qa_prompt=CYPHER_QA_PROMPT,
    validate_cypher=True,
)
