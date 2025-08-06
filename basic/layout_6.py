import streamlit as st
import pandas as pd
import os

#side bar
df = pd.read_csv(f'{os.path.dirname(os.path.abspath(__file__))}/data/sample.csv')
with st.sidebar:
  st.write("hello side bar")
  radio = st.radio("pick a colum", options=df.columns[1:], index=0)
  st.write(radio)

col1, col2, col3 = st.columns(3)
col1.write("text in a column")
slider = col2.slider("slider",min_value=0, max_value=10, value=2, step=1)
col3.write(slider)

tab1, tab2 = st.tabs(["line plot", "bar plot"])
with tab1:
  tab1.write("A plot line")
  st.line_chart(df, x="year", y=["col1", "col2", "col3"])

with tab2:
  tab1.write("Bar chart")
  st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

with st.expander("Click to expand"):
  st.write("I am text that you see when you expand")