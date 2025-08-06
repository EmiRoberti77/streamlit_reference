import streamlit as st
import pandas as pd
import os

# Buttoms
primary_btn = st.button(label="Primary", type="primary")
secondary_btn = st.button(label="Secondary", type="secondary")
tertiary_btn = st.button(label="Tertiary", type="tertiary")
if primary_btn:
  st.write("Hello from primary")

if secondary_btn:
  st.write("Hello from secondary")

if tertiary_btn:
  st.write("Hello from tertiary")

st.divider()

checkbox = st.checkbox("Remember me")
if checkbox:
  st.write("I will remember you")
else:
  st.write("I will forget you")

st.divider()

df = pd.read_csv(f"{os.path.dirname(os.path.abspath(__file__))}/data/sample.csv")

radio = st.radio("Choose a column", options=df.columns[1:], index=0, horizontal=True)
st.write(radio)

st.divider()

select = st.selectbox("Choose a colum", options=df.columns[1:], index=0 )
st.write(select)

st.divider()
multi_select = st.multiselect("Choose columns", options=df.columns[1:], default=["col1"], max_selections=3)
st.write(multi_select)

st.divider()
slider = st.slider("pick a number", min_value=0, max_value=10, value=5, step=1)
st.write(slider)

st.divider()
num_input = st.number_input("Pick a number", min_value=0, max_value=10)
st.write(f"You picked {num_input}")
text_input = st.text_input("Write something", value="hello")
st.write(f"you wrote {text_input}")
text_area = st.text_area("text area", height=300, width=600)
st.write(text_area)
st.divider()