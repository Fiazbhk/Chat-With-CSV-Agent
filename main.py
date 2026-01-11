import streamlit as st
from langchain import OpenAI
from langchain_experimental.agents import create_csv_agent
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

st.title("Chat With CSV Agent")

uploaded_file = st.file_uploader("Choose a file", type=["csv"])
if uploaded_file is not None:
    csv_file_path = uploaded_file.name
    with open(csv_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    df = pd.read_csv(csv_file_path)
    st.write("Uploaded CSV File")
    st.dataframe(df)

    agent = create_csv_agent(OpenAI(), csv_file_path, verbose=True, allow_dangerous_code=True)

    query = st.text_input("Ask your query")

    if query:
        response = agent.run(query)
        st.write("Answer")
        st.write(response)