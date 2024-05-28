import pandas as pd
from pandasai import Agent, config, SmartDataframe
from pandasai.llm import OpenAI

import streamlit as st


llm = OpenAI(api_token="sk-proj-jNKWINpwa2RL5V4W102LT3BlbkFJb6dmcRii3ewlKHPmw8KP")


class CSVPandas:
    def __init__(self, llm):
        self.llm = llm

    def display(self):
        st.title("Pandas AI and CSV Files")

        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            st.write(data.head(3))

            df = SmartDataframe(data, config={"llm": llm})

            prompt = st.text_area("Enter A Prompt For The CSV:")

            if st.button("Generate Response"):
                if prompt:
                    with st.spinner("Generating data..."):
                        st.write(df.chat(prompt))
