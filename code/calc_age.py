# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 10:47:21 2016

@author: wayne
Calculate age at time of entry for every row and add a new column
This way we can do group stats by age easily
This will also allow us to see what kIDs we don't have in the web data
Store in days old: w = (x-y).days
Will need to first convert startTime columns to_datetime
i.e. data_merged['startTime'] = pd.to_datetime(data_merged['startTime'],errors='coerce')
e=(k==6332083474006016).nonzero()
Need to find which kIDs are strings and remove them
"""
k_dob = []
register_info_table.kID = pd.to_numeric(register_info_table.kID,errors='coerce')

for row in kid_table.kID:
    m = register_info_table[register_info_table.kID==row]
    if len(m) == 0:
        k_dob.append('Not Found')
    else:            
        e = register_info_table[register_info_table.kID==row].index[0]
        k_dob.append(register_info_table.DOB[e])
        
k_dob = pd.Series(k_dob)