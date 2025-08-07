import streamlit as st
import time
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Caching demonstration")

st.button("Test Cache")

st.subheader('st.cache_data')
"""
this decorator will cache the function so that every user 
interaction it will not run again
"""
@st.cache_data
def cache_this_function():
  time.sleep(3)
  out = "I am done running"
  return out

out = cache_this_function()
st.write(out)

st.subheader('st.cache_resources')

"""
this decorator will cache the resources so that every user 
interaction it will not run again
"""
@st.cache_resource
def create_simple_linear_regression():
  time.sleep(3)
  x = np.array([1,2,3,4,5,6,7,8,9]).reshape(-1, 1)
  y = np.array([1,2,3,4,5,6,7,8,9])
  model = LinearRegression().fit(x,y)
  return model

lr = create_simple_linear_regression()
X_pred = np.array([8]).reshape(-1,1)
pred = lr.predict(X_pred)
st.write(f"The prediction is:{pred[0]}")
