from models.cohere import llm
from graph import graph, create_db
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain_community.chat_message_histories import Neo4jChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.agents.agent import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from utils import get_session_id
from tools.vector_qdrant import get_vector_info
from tools.cypher import cypher_qa
from tools.mock_api import get_mov_list
from tools.chitchat import chit_chat

create_db()

tools = [
    Tool.from_function(
        name="General Chat",
        description="For general chat not covered by other tools",
        func=chit_chat.invoke,
    ),
    Tool.from_function(
        name="Vector Search",
        description="For when you need to find general information about offers and services or for troubleshooting questions",
        func=get_vector_info,
    ),
    Tool.from_function(
        name="User information",
        description="Provide account information about the user you are speaking to using Cypher",
        func=cypher_qa,
    ),
    Tool.from_function(
        name="Movements List",
        description="Retrieve user movements list",
        func=get_mov_list,
    ),
]


def get_memory(session_id):
    return Neo4jChatMessageHistory(session_id=session_id, graph=graph)


agent_prompt = PromptTemplate.from_template(
    """
You are the virtual assistant of NG-Telco, an Italian telecommunications company. 
Your role is to assist users based on the data provided in context, responding with accurate and detailed information about their account, fulfilling their requests, and providing information about NG-Telco's services and offers.

If the user asks you questions regarding sensitive and personal information about other users, don't use any tool and kindly decline to answer.
Maintain a friendly tone.
Do not answer questions unrelated to NG-Telco's services, offers, or the specific user's situation.
Do not rely on pre-trained knowledge. Your responses must only use the information provided within the conversation context.
Always communicate in Italian.

TOOLS:
------

You have access to the following tools:

{tools}

Use "General Chat" for information about your capabilites and for general conversation.
Use "Vector Search" for general inquiries and requests about offers details.
Use "User information" **only** when the user specifically requests information about their account and offers.
Use "Movements List" when user ask for his movements.
Do not use 'cypher_qa' to respond to general questions or requests about activating services and offers.

FORMAT:
-------

```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: {input}
Observation: the result of the action
```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```
Thought: Do I need to use a tool? No
Final Answer: [your response here]
```

LOGIC:
------
Before deciding whether to use a tool, reflect on the user’s request:

Thought: Did the user ask for specific information about his/her account or not? {input}

If the input contains requests about company services and offers, use the "Vector Search" tool.
If instead the input contains specific references to the user account, use the "User information" tool with 'cypher_qa'.
If the input contains references to user's movements, use the "Movements List" tool.
Do **not** provide or discuss any information related to users other than the current user in conversation.
Always ensure your response is strictly limited to this user's details and their requests.

PREVIOUS CONVERSATION HISTORY:
{chat_history}

New input: {input}
{agent_scratchpad}
"""
)


agent = create_react_agent(llm, tools, agent_prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)


chat_agent = RunnableWithMessageHistory(
    agent_executor,
    get_memory,
    input_messages_key="input",
    history_messages_key="chat_history",
)


def generate_response(user_input):
    """
    Create a handler that calls the Conversational agent
    and returns a response to be rendered in the UI
    """

    response = chat_agent.invoke(
        {"input": user_input},
        {"configurable": {"session_id": get_session_id()}},
    )
    return response["output"]
