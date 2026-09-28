from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

model=ChatMistralAI(model='mistral-small-2506')

prompt = ChatPromptTemplate.from_messages(
    [
      ('system', """
You are an expert content summarizer. 

Read the following text carefully and generate: 
1. A short and meaningful title. 
2. A concise summary of the text. 
Rules: - The title should be short and relevant. 
- The summary should be 3-5 sentences. 
- Use simple and professional language. 
- Include only the important information. 
- Do not add information that is not present in the text. 

Return the response in this format: 
Title: <generated title> Summary: <generated summary>
    """),

      ('human', " {paragraph} ")
    ]
)

while True:
    para = input("give your paragraph: ")
    if para == "0":
        print("AI: Goodbye! 👋")
        break
    final_promt = prompt.invoke(
        {"paragraph"  : para}
        )

    response = model.invoke(final_promt)
    print( "\n\n\n", "AI: ", response.content)