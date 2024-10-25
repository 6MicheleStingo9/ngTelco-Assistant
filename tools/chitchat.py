from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from models.cohere import llm

chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are NG-Telco's virtual assistant, an Italian telecommunications company.
            Provide help and general information about your capabilities namely: finding information about users personal
            situation and movements and help them with troubleshooting question. 
            """,
        ),
        ("human", "{input}"),
    ]
)

chit_chat = chat_prompt | llm | StrOutputParser()
