# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:33:29 2015

@author: wayne
"""

# import numpy as np
import pandas as pd
import matplotlib
matplotlib.style.use('ggplot')

# setup io file names
inFile = "/Users/wayne/Downloads/nyu-160503-6.csv"
inFile2 = "/Users/wayne/Downloads/Archive/clean_merged_new.csv"
outFile = "/Users/wayne/Downloads/Archive/clean_merged_new.csv"

# load csv
hdr = ['kidID', 'entryID', 'startTime', 'endTime', 'activity','durationMin','quantity','extraData','text','notes','caregiver','childName']
data = pd.read_csv(inFile, header=0, names=hdr,error_bad_lines=False,quoting=3)
data2 = pd.read_csv(inFile2, header=0, names=hdr,error_bad_lines=False,quoting=3)

data_merged = [data, data2]
data_merged = pd.concat(data_merged)

# clean and organize data
# convert timestamps to date/time datatype
data_merged['startTime'] = pd.to_datetime(data_merged['startTime'],errors='coerce')
data_merged['endTime'] = pd.to_datetime(data_merged['endTime'],errors='coerce')

# sort by kidID -> startTime
data_merged.sort_index(by=['kidID', 'startTime'])

# get sleep duration data from 1 kid
# df = data_merged['durationMin']

# filter duration data and plot
# filtered = df[(data_merged['activity'] == "Sleep")]
# filtered.plot(kind='hist', alpha=0.5)

# g = data_merged.groupby('startTime')

# save merged file to csv
data_merged.to_csv(outFile)