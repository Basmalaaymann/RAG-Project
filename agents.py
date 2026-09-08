from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

llm = ChatOllama(
    model="llama3.1",
    temperature=0,
) 

def retriever_agent(state: State):
    user_input= state.get('rewritten_query')
    embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2") #same embeddings done during webscrapping
    
    vdb= Chroma(
        
    )
        
        