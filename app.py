import streamlit as st
from post_pandas import PostPandas
from csv_pandas import CSVPandas
from pandasai.llm import OpenAI


llm = OpenAI(api_token="")

st.set_page_config(layout="wide")

st.sidebar.header("About")
st.sidebar.write("Investigation into the uses of PandasAI")

tabs = st.tabs(["Postgres", "CSV File"])

# Display content in each tab
with tabs[0]:
    post_pandas = PostPandas(llm)
    post_pandas.display()

with tabs[1]:
    csv_pandas = CSVPandas(llm)
    csv_pandas.display()
