# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:10:01 2016

@author: wayne
"""

import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
# Get list of kids first
conn = sqlite3.connect("babysleep.db")
data = pd.read_sql_query("SELECT kID from Register_Info", conn)

# verify that result of SQL query is stored in the dataframe
print data.head()

conn.close()