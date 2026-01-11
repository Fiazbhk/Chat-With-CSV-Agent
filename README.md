# Chat With CSV Agent

A Streamlit web application that allows users to upload a CSV file and interact with it using natural language queries powered by LangChain and OpenAI.

---

## Overview

This application enables:
- CSV file upload through a browser interface
- Automatic parsing and preview of tabular data
- Natural language querying over CSV contents
- Responses generated via a LangChain CSV agent backed by OpenAI

The app is deployed on **Streamlit Cloud** and requires no local setup for end users.

---

## Architecture

User
└─ Browser (Streamlit UI)
├─ CSV Upload
├─ Data Preview (pandas)
└─ Query Input
↓
LangChain CSV Agent
↓
OpenAI LLM
↓
Natural Language Answer


---

## Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **LangChain**
- **LangChain OpenAI Provider**
- **OpenAI API**

---

## Project Structure

├── main.py # Streamlit application entry point
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## Deployment

The app is deployed using **Streamlit Cloud**.


---

## Deployment

The app is deployed using **Streamlit Cloud**.

### Deployment Requirements

- GitHub repository
- `requirements.txt` present at root
- OpenAI API key stored in Streamlit Secrets

**Environment Variable**


---

## Local Development

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_openai_api_key
streamlit run main.py

```

## Usage

- Upload a CSV
- Review the data
- Ask a question
- Get an answer derived from the dataset

## Core Idea

This project is not about chat.

It is about **reducing the distance between a question and a verified answer in data**.
