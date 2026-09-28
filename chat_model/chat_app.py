import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


# Model
model = ChatMistralAI(model="mistral-small-2506")


# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert content summarizer.

Read the following text carefully and generate:
1. A short and meaningful title.
2. A concise summary of the text.

Rules:
- The title should be short and relevant.
- The summary should be 3-5 sentences.
- Use simple and professional language.
- Include only the important information.
- Do not add information that is not present in the text.

Return the response in this format:

Title: <generated title>

Summary: <generated summary>
            """,
        ),
        ("human", "{paragraph}"),
    ]
)


# UI
st.title("AI Title and Summary Generator")

paragraph = st.text_area(
    "Give your paragraph:",
    height=200
)

if st.button("Generate"):
    final_prompt = prompt.invoke(
        {"paragraph": paragraph}
    )

    response = model.invoke(final_prompt)

    st.write(response.content)