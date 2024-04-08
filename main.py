import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Chat with Database")

question = st.text_input("Question: ")

if question:
    chain, query = get_few_shot_db_chain()
    response_query = query.invoke({"question": f"{question}"})
    response = chain.invoke({"question": f"{question}"})

    st.header("SQL Query")
    st.write(response_query +";")
    st.header("Answer")
    st.write(response)
