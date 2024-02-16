#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import sqlite3
import pandas as pd
import sql
from prompts.prompts import SYSTEM_MESSAGE
from prompts.prompts_1 import SYSTEM_MSG
from open_ai import get_completion_from_messages
from open_ai import get_complete
import json
import ast
import re


def query_database(query, conn):
    """ Run SQL query and return results in a dataframe """
    return pd.read_sql_query(query, conn)

# Create or connect to SQLite database
conn = sql.create_connection()

# Schema Representation for finances table
schemas = sql.get_schema()
#print(schemas)
st.title("SQL Query Generator with GPT-3.5")
st.write("Enter your message to generate SQL and view results.")

# Input field for the user to type a message
user_message = st.text_input("Enter your message:")

if user_message:
    # Format the system message with the schema
    #formatted_system_message = SYSTEM_MESSAGE.format(schema=schemas['finances'])
    formatted_system_message = SYSTEM_MESSAGE.format(schema=schemas)

    # Use GPT-4 to generate the SQL query
    response = get_completion_from_messages(formatted_system_message, user_message)
    #json_response = json.loads(response)
    #query = json_response['query']

    # Display the generated SQL query
    st.write("Generated SQL Query:")
    st.code(response, language="sql")

    try:
        # Run the SQL query and display the results
        sql_results = query_database(response, conn)
        print('sql_res',sql_results)
        st.write("Query Results:")
        st.dataframe(sql_results)
        graph = get_complete(SYSTEM_MSG, sql_results)
        
        x = re.search("import", graph)
        graph = graph[x.start():]
        print('graph',graph)
        exec(graph)

    except Exception as e:
        st.write(f"An error occurred: {e}")

