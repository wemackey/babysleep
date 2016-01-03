# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:08:51 2016

@author: wayne
"""

import sqlite3
import pandas as pd

# setup io file names
inFile = "/Users/wayne/Downloads/Archive/clean_merged.csv"

# load csv
hdr = ['kidID', 'entryID', 'startTime', 'endTime', 'activity','durationMin','quantity','extraData','text','notes','caregiver','childName']
data = pd.read_csv(inFile, header=0, names=hdr)

# create new db and make connection
conn = sqlite3.connect('babysleep_test.db')
conn.text_factory = str

# make sure dataframe exists
data.to_sql(con=conn, name='sleep_data', if_exists='replace', flavor='sqlite')

# close connection
conn.close()