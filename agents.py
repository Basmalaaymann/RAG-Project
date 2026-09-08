from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage
from prompts import *
from models import *


llm = ChatOllama(
    model="llama3.1",
    temperature=0,
) 

def retriever_agent(state: State):
    user_input= state.get('rewritten_query')
    embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2") #same embeddings done during webscrapping
    
    vdb= Chroma(
        presist_directory = 'egyption_private_schools',
        embedding_function = embeddings
    )
    retriever = vdb.as_retriever(search_kwargs={'k':10})
    result = retriever.invoke(user_input)
    return{
        "context": result
    }
    
    

def rewritten_query(state: State):
    user_input = state.get("query")
    chat_hist = state.get("chat_history")
    
    messages = [
        SystemMessage(content = 'REWRITE_PROMPT'),
        HumanMessage(content = query_rewrite_extend(user_input , chat_hist))
    ]
    
    response= llm.invoke(messages)
    rewritten_query = response.content.strip()
    return{
        rewritten_query: "rewritten_query"
    } 


def response_agent(state:State):
    chat_history= state.get('chat_history')
    rewritten_query = state.get('rewritten_query')
    context = state.get('context')
    
    messages= [
        SystemMessage(content= "SYSTEM_PROMPT"),
        HumanMessage(content= system_prompt_extend(rewritten_query ,context, chat_history))
    ]
    
    response = llm.invoke(messages)
    final_response = response.content.strip()
    return{
        final_response: "response"
    }