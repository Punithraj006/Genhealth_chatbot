#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.title("SQL Query Generator with GPT-4")
st.write("Enter your message to generate SQL and view results.")
user_message = st.text_input("Enter your message:")

