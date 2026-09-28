from dotenv import load_dotenv

load_dotenv()

#option-1
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

#llm = HuggingFaceEndpoint(
    #repo_id="deepseek-ai/DeepSeek-V4-Flash-0731")

model = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731"
    ))


response = model.invoke("what is your name")
print(response.content)


#option-2
'''from langchain.chat_models import init_chat_model

model = init_chat_model(
    "deepseek-ai/DeepSeek-V4-Flash-0731"
    model_provider="huggingface"
)'''