from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

model=ChatMistralAI(model='mistral-small-2506')

class movie(BaseModel):
    title: str 
    release_year : Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object = movie)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
You are an expert information extraction assistant.
Return ONLY valid JSON.
Do not use Markdown.
Do not add explanations.
"""),

("human", """
Extract information from this movie description:

{movie}
    )

{format_instructions}
""")
    ]
)

while True:

    para = input("Give your paragraph: ")

    if para == "0":
        print("AI: Goodbye! 👋")
        break

    final_prompt = prompt.invoke(
        {
            "movie": para,
            "format_instructions": parser.get_format_instructions()
        }
    )

    response = model.invoke(final_prompt)

    movie_data = parser.parse(response.content)

    print(movie_data)