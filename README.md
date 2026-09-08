# 🏫 Egyptian Private Schools & Universities Agentic RAG

An end-to-end, privacy-focused Retrieval-Augmented Generation (RAG) system built with **LangGraph**, **Ollama (Gemma 3)**, and **Streamlit**. 

This application serves as an intelligent educational consultant, answering complex user inquiries about private schools and universities in Egypt with context-grounded accuracy and conversational awareness.

---

## 🌟 Key Features

* **Agentic Multi-Step Workflow:** Utilizes a stateful graph (`StateGraph`) using **LangGraph** rather than linear chains to process queries dynamically.
* **Context-Aware Query Rewriting:** Automatically reformulates ambiguous or follow-up user inputs into standalone search queries based on the chat history.
* **Privacy-First & Open-Source Stack:** Runs entirely locally using **Ollama (Gemma 3)** for LLM reasoning and **ChromaDB** for vector storage.
* **Domain-Specific Prompting:** Enforces strict system prompt guardrails to eliminate hallucinations and adhere strictly to Egyptian higher education domain knowledge.
* **Interactive UI:** A full-featured **Streamlit** chat application with persistence, conversation clearing, and sidebar guidance.

---

## 🏗️ System Architecture

The LangGraph workflow consists of three dedicated stateful nodes:
1. **`rewritten_query_agent`**: Processes user input alongside session chat history using `Gemma 3` to produce a clear, standalone query.
2. **`retriever_agent`**: Queries the persistent **ChromaDB** vector database utilizing HuggingFace embeddings (`all-MiniLM-L6-v2`) to retrieve the top 10 relevant document chunks (`k=10`).
3. **`response_agent`**: Synthesizes a structured, accurate response strictly grounded in the retrieved context.

---

## 🛠️ Tech Stack

* **Frameworks & Orchestration:** `LangChain`, `LangGraph`
* **Large Language Model (LLM):** `Gemma 3:latest` via `Ollama`
* **Vector Store:** `ChromaDB`
* **Embeddings:** `HuggingFace` (`sentence-transformers/all-MiniLM-L6-v2`)
* **User Interface:** `Streamlit`
* **Language:** Python 3.10+

---

## 📂 Project Structure

```text
├── agents.py       # Agent node definitions (Rewriter, Retriever, Response Generator)
├── app.py          # Streamlit UI interface & conversation management
├── models.py       # State definitions (TypedDict schema for LangGraph)
├── prompts.py      # System prompts and prompt template extension helpers
├── workflow.py     # StateGraph architecture and execution logic
└── requirements.txt# Project dependencies
