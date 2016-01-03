# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:21:12 2015

@author: wayne
"""

import pandas as pd

# setup io file names
inFile = "/Users/wayne/Downloads/Archive/clean_merged.csv"

# load csv
hdr = ['kidID', 'entryID', 'startTime', 'endTime', 'activity','durationMin','quantity','extraData','text','notes','caregiver','childName']
data = pd.read_csv(inFile, header=0, names=hdr)

