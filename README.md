# AI Engineering Journey – Chatbot v1

## Overview

This project is the first milestone in my AI Engineering learning journey.

It is a command-line chatbot built using **Python**, **LangChain**, and the **Groq API**. The chatbot supports continuous conversations by maintaining chat history, allowing the AI to remember previous messages during the session.

The objective of this project is to understand the fundamentals of LLM integration before moving toward advanced topics such as prompt engineering, RAG, agents, LangGraph, and enterprise AI systems.

---

## Features

* Continuous chat using `while True`
* Conversation memory using chat history
* Uses `HumanMessage` and `AIMessage`
* Exit commands (`exit`, `quit`)
* Input validation
* Environment variable support with `.env`
* Groq LLM integration using LangChain

---

## Tech Stack

* Python 3.x
* LangChain
* LangChain Groq
* python-dotenv
* Groq API

---

## Project Structure

```text
.
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
python app.py
```

Example:

```text
Ask me anything: My name is Anmol.

AI: Nice to meet you, Anmol.

Ask me anything: What's my name?

AI: Your name is Anmol.
```

---

## Learning Outcomes

This project helped me understand:

* Environment variables
* API key management
* LLM integration
* LangChain basics
* Chat history
* HumanMessage
* AIMessage
* Stateful conversations
* Python loops and control flow

---

## Future Improvements

* SystemMessage support
* Prompt templates
* Streaming responses
* Conversation persistence
* Vector database integration
* Retrieval-Augmented Generation (RAG)
* Agent workflows with LangGraph
* FastAPI backend
* Web interface

---

## Learning Journey

This repository is part of my AI Engineering roadmap, where I build projects from first principles to gain a deep understanding of AI systems, software architecture, and enterprise-scale applications.

Each project focuses on learning the underlying concepts rather than only using frameworks.

---

## License

This project is created for learning and educational purposes.
