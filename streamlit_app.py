
import streamlit as st
import pandas as pd

st.title("SlowAPI")

query_params = st.experimental_get_query_params()
#st.write(query_params)

if "user" not in st.session_state:
    st.session_state.user = 1

if "method" in query_params:
    if query_params["method"][0]=="post":
        #st.write(query_params)
        user = query_params["user"][0]
        st.write(f"post user {user}")
        with open("file.txt", "a") as fh:
            fh.write(f"post user {user}\n")
        st.write(f"Wrote to file")
        st.session_state.user += 1
        st.experimental_set_query_params()
else:
    st.write("Just the regular website")
    #st.write(query_params)