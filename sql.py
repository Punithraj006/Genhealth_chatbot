#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import heapq
import sqlite3
# import csvkit

import pandasql as ps
import sqlalchemy
# from quickchart import QuickChart
import requests
import json

final_df = pd.read_csv(r'final2.csv')
lung_df = pd.read_csv(r'lungs2.csv')
cardio_df = pd.read_csv(r'cardio2.csv')
diabetes_df = pd.read_csv(r'diabetes2.csv')

DATABASE_NAME = "mydatabase.db"


""" Create or connect to an SQLite database """
def create_connection():
    """ Create or connect to an SQLite database """
    conn = None;
    try:
        conn = sqlite3.connect(DATABASE_NAME)
    except Error as e:
        print(e)
    return conn



def get_schema():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    db_schema = {}
    
    for table in tables:
        table_name = table[0]
        
        # Query to get column details for each table
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        
        column_details = {}
        for column in columns:
            column_name = column[1]
            column_type = column[2]
            column_details[column_name] = column_type
        
        db_schema[table_name] = column_details
    
    conn.close()
    return db_schema


# In[11]:




