import streamlit as st
import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from workflow import Workflow
from models import State
from langchain_core.messages import HumanMessage

# Set page config
st.set_page_config(
    page_title="Egyptian Private Schools RAG",
    page_icon="🏫",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# App title and description
st.title("🏫 Egyptian Private Schools Information System")
st.markdown("Ask questions about Egyptian private schools and universities!")

# Sidebar for info
with st.sidebar:
    st.header("About")
    st.markdown("""
    This RAG system uses LangGraph to:
    1. **Rewrite** your query for better understanding
    2. **Retrieve** relevant information from our database
    3. **Generate** comprehensive answers about Egyptian private schools
    """)
    
    st.header("Examples")
    st.markdown("""
    - What are the best private schools in Cairo?
    - Tell me about tuition fees for international schools
    - Which schools offer IB programs?
    - What are the admission requirements?
    """)
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about Egyptian private schools..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Processing your query..."):
            try:
                # Prepare the state
                chat_history = [HumanMessage(content=msg["content"]) for msg in st.session_state.messages[:-1]]
                
                initial_state = State(
                    chat_history=chat_history,
                    query=prompt,
                    context=None,
                    response="",
                    rewritten_query=""
                )
                
                # Run the workflow
                result = Workflow().run(initial_state)
                
                # Extract the response
                response = result.get("response", "I couldn't generate a response. Please try again.")
                
                # Display response
                st.markdown(response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Footer
st.markdown("---")
st.markdown("*Powered by LangGraph and Streamlit*") 