# type: ignore
import os
from typing import TextIO

import openai
import pandas as pd
import streamlit as st
from langchain.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.llms import OpenAI

# openai.api_key = st.secrets["OPENAI_API_KEY"]


def get_answer_csv(file_path: str, query: str) -> str:

    df = pd.read_csv("sale.csv")

    # Create an agent using OpenAI and the Pandas dataframe
    # agent = create_csv_agent(OpenAI(temperature=0), file, verbose=False)
    agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)

    # Run the agent on the given query and return the answer
    #query = "whats the square root of the average age?"
    answer = agent.run(query)
    return answer
