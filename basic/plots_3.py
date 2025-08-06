import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

path_standard = f"{os.path.dirname(os.path.abspath(__file__))}/data/sample.csv"
path_geo= f"{os.path.dirname(os.path.abspath(__file__))}/data/sample_map.csv"

df = pd.read_csv(path_standard)
# Streamlit line plt
st.line_chart(df, x="year", y=["col1", "col2", "col3"])
# Streamlit area chart
st.area_chart(df, x="year", y=["col1", "col2", "col3"])
# Streamlit bar chart
st.bar_chart(df, x="year", y=["col1", "col2", "col3"] )
# Streamlit map
geo_df = pd.read_csv(path_geo)
st.map(geo_df)
# Matplotlib
fig, ax = plt.subplots()
ax.plot(df.year, df.col1)
ax.set_title("My figure title")
ax.set_xlabel("x label")
ax.set_ylabel("y label")
fig.autofmt_xdate()
st.pyplot(fig)