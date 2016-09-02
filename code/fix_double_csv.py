# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:36:44 2016

@author: wayne
"""

import pandas as pd

# from baby info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/db/webform_views_baby_info20160130120006.csv"

# load baby info csv
hdr = (['sID','x1','uID','x2','birthOrder','x3','ofTotalBorn','x4','within2Weeks','x5','weeksEarly',
        'x6', 'weeksLate','x7','progress','x8','email','x9','kID','x10','kidRace','x11','ethnicity','x12','birthCity',
        'x13','seriousInjury','x14','describeInjury','x15','earInfection','x16','timeSinceEarInfection',
        'x17','hearingLoss','x8','describeHearingLoss','x19','timeStamp','ip','x20',])
data = pd.read_csv(inFile, header=0, names=hdr)
