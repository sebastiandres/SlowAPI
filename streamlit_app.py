
import streamlit as st
import pandas as pd

st.title("SlowAPI")

query_params = st.experimental_get_query_params()

if "method" in query_params:
    if query_params["method"][0]=="post":
        user = query_params["user"][0]
        st.write(f"post user {user}")
        with open("file.txt", "a") as fh:
            fh.write(f"{user}\n")
        st.write(f"Wrote user to file")
        st.experimental_set_query_params()
else:
    st.write("Just the regular website")

if st.button("Show File"):
    with open("file.txt", "r") as fh:
        st.write("\n".join(fh.readlines()))