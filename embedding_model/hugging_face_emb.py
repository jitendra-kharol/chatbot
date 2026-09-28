from langchain_huggingface import HuggingFaceEmbeddings

embeddings_model  = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L3-v2",
)

#text=("hello")

vector=embeddings_model.embed_query("hello")
print(vector)