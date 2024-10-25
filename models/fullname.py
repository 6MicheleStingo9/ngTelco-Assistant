from pydantic import BaseModel, Field, field_validator
from models.cohere import llm
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate


class Fullname(BaseModel):
    """Fullname of the user"""

    name: str = Field(..., description="The name of the user")
    surname: str = Field(..., description="The surname of the user")

    @field_validator("name", "surname", mode="before")
    def lowercase_string(cls, v: str) -> str:
        return v.lower() if isinstance(v, str) else v


# Set up a parser
parser = PydanticOutputParser(pydantic_object=Fullname)

# Prompt
prompt = ChatPromptTemplate.from_template(
    template="""
    Retrieve the name and surname of the user from the given context
    Provide the output in JSON format\n{format_instructions}
    """,
).partial(
    format_instruction=parser.get_format_instructions(),
)

chain = prompt | llm | parser


def getFullname(query):
    return chain.invoke(query)
