# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:21:12 2015

@author: wayne
"""

#import numpy as np
import pandas as pd
import matplotlib
matplotlib.style.use('ggplot')

# setup io file names
inFile = "/Users/wayne/Downloads/Archive/clean_merged.csv"

# load csv
hdr = ['kidID', 'entryID', 'startTime', 'endTime', 'activity','durationMin','quantity','extraData','text','notes','caregiver','childName']
data = pd.read_csv(inFile, header=True, names=hdr)

# clean and organize data
# convert timestamps to date/time datatype
data['startTime'] = pd.to_datetime(data['startTime'],errors='coerce')
data['endTime'] = pd.to_datetime(data['endTime'],errors='coerce')

# sort by kidID -> startTime
data.sort_index(by=['kidID', 'startTime'])

# remove duplicate entries

# check if other activities occur while kid is asleep

# get sleep duration data from 1 kid
# first get all kidIDs
list_kIDs = pd.unique(data.kidID.ravel())

# print out all kidIDs
for kID in range(0,len(list_kIDs)):
    print list_kIDs[kID]
    
# select first kid for testing purposes
data_kID = data[data.kidID == list_kIDs[1]]
data_kID.index = data_kID.startTime

# plot sleep data across time
df = data_kID.durationMin
sleepDur = df[(data_kID['activity'] == "Sleep")]
sleepDur[sleepDur>180].plot()

g = data_kID.groupby('startTime')

# filter duration data and plot
df = data['durationMin']
filtered = df[(data['activity'] == "Sleep")]
filtered.plot(kind='hist', alpha=0.5)

data['quantity'].plot(kind='hist', alpha=0.5)


# segment by day
# plot 

# segment by hour
# plot

# save file

# combine months