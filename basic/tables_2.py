import streamlit as st
import pandas as pd
import os
import sys
path = os.path.dirname(os.path.abspath(__file__)) + '/data/sample.csv'
print(path)
df = pd.read_csv(path, dtype=int)
st.dataframe(df)
st.write(df)
st.table(df)

st.metric(label="Metric Label", value=900, delta=-0.1, delta_color="normal")
st.metric(label="Expenses", value=456, delta=-0.7, delta_color="inverse")