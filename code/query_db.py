# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 10:32:44 2016

@author: wayne
"""

import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
conn = sqlite3.connect("babysleep_test.db")
data = pd.read_sql_query("SELECT * from sleep_data", conn)

# verify that result of SQL query is stored in the dataframe
print data.head()

conn.close()