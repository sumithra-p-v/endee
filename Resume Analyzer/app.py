import streamlit as st
from rag import add_document, search

st.title("AI Resume Analyzer")

# input resume
resume = st.text_area("Paste your resume here")

if st.button("Store Resume"):
    add_document(resume)
    st.success("Resume stored!")

# query
query = st.text_input("Ask something about your resume")

if st.button("Search"):
    if query:
        result = search(query)
        st.write("Result:")
        st.write(result)