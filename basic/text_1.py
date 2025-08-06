import streamlit as st
#set title
st.title("Emi Title")
# Header
st.header("Main header")
# Subheader
st.subheader("Sub header")
# Markdown
st.markdown("this is markdown text")
st.markdown("# Header 1")
st.divider()
st.markdown("## Header 2")
st.divider()
st.markdown("### Header 3")
st.markdown("this is markdown text")
# Caption
st.caption("this is Emi's caption")
# Code
st.code("""
print("hello")
""")
# Latex
st.latex("x = 2^2")
# Divider
st.divider()
#st.write
data = [1,2,3,4,5,6]
st.write("data", data)