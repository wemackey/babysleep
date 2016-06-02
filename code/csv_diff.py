# -*- coding: utf-8 -*-
"""
Created on Fri May  6 23:12:43 2016

@author: wayne
20160515060010 as timestamp for comparison
20160505180005 as timestamp for backup
Total of 6 tables to check
"""

import pandas as pd
# import numpy as np

######################
# REGISTER YOUR BABY #
######################

# Specify input CSV files
inFile1 = "/Users/wayne/babysleep/test_dump/webform_views_register_your_baby_for_the_research_study20160515060010.csv"
inFile2 = "/Users/wayne/babysleep/backup_5_5_16/webform_views_register_your_baby_for_the_research_study20160505180005.csv"

# Specify header organization
hdr = (['sID', 'uID', 'instructions', 'instructions1', 'instructions2','instructions3', 'email', 
        'kID','instructionsKid','DOB','gender','firstName','middleInitial','instructions4',
        'instructions5','instructions6','timeStamp','ip'])
        
# Load into dataframes
data1 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)
data2 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)

isSame_register_your_baby = data1.equals(data2)

# if they are not the same, tell me what is different
# if isSame_register_your_baby == False:
#     diff_inds_register_your_baby = data1 != data1
#     changedids_register_your_baby = data1.index[np.any(data1 != data2,axis=1)]

#############
# BABY INFO #
#############
   
# Specify input CSV files
inFile1 = "/Users/wayne/babysleep/test_dump/webform_views_baby_info20160515060010.csv"
inFile2 = "/Users/wayne/babysleep/backup_5_5_16/webform_views_baby_info20160505180005.csv"

# Specify header organization
hdr = (['sID', 'uID', 'birthOrder', 'ofTotalBorn', 'del_me','pounds', 'ounces', 
        'within2Weeks','weeksEarly','weeksLate','progress','email','kID','kidRace', 'specifyRace',
        'ethnicity','birthCity','seriousInjury','describeInjury','earInfection',
        'timeSinceEarInfection','hearingLoss','describeHearingLoss','timeStamp','ip'])
        
# Load into dataframes
data1 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)
data2 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)

isSame_baby_info = data1.equals(data2)

###########################
# BIOLOGICAL SIBLING INFO #
###########################
   
# Specify input CSV files
inFile1 = "/Users/wayne/babysleep/test_dump/webform_views_biological_sibling_info20160515060010.csv"
inFile2 = "/Users/wayne/babysleep/backup_5_5_16/webform_views_biological_sibling_info20160505180005.csv"

# Specify header organization
hdr = (['sID', 'uID', 'bs1FirstName', 'bs2FirstName', 'bs3FirstName','bs4FirstName', 'bs5FirstName', 
        'bs6FirstName','bs7FirstName','bs8FirstName','bs9FirstName','bs1MiddleInitial','bs2MiddleInitial',
        'bs3MiddleInitial', 'bs4MiddleInitial','bs5MiddleInitial', 'bs6MiddleInitial','bs7MiddleInitial',
        'bs8MiddleInitial','bs9MiddleInitial','bs1DOB','bs2DOB','bs3DOB','bs4DOB','bs5DOB','bs6DOB',
        'bs7DOB','bs8DOB','bs9DOB','bs1Gender','bs2Gender','bs3Gender','bs4Gender','bs5Gender',
        'bs6Gender','bs7Gender','bs8Gender','bs9Gender','bs1AddSibling','bs2AddSibling','bs3AddSibling',
        'bs4AddSibling','bs5AddSibling','bs6AddSibling','bs7AddSibling','bs8AddSibling','bs9AddSibling',
        'email','kID','anySiblings','timeStamp','ip'])
        
# Load into dataframes
data1 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)
data2 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)

isSame_biological_sibling_info = data1.equals(data2)

##################
# DIAGNOSIS INFO #
##################
   
# Specify input CSV files
inFile1 = "/Users/wayne/babysleep/test_dump/webform_views_child_diagnosis20160515060010.csv"
inFile2 = "/Users/wayne/babysleep/backup_5_5_16/webform_views_child_diagnosis20160505180005.csv"

# Specify header organization
hdr = ['sID', 'uID', 'email', 'kID', 'diagnosis','other', 'timestamp','ip'] 

# Load into dataframes
data1 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)
data2 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)

isSame_diagnosis_info = data1.equals(data2)

###############
# PARENT INFO #
###############
   
# Specify input CSV files
inFile1 = "/Users/wayne/babysleep/test_dump/webform_views_parent_info20160515060010.csv"
inFile2 = "/Users/wayne/babysleep/backup_5_5_16/webform_views_parent_info20160505180005.csv"

# Specify header organization
hdr = (['sID','uID','numAdults','numChildren','spouseRelationship','spouseRelationshipOther',
        'spouseDOB','fatherDOB','spouseEmploymentStatus','fatherCityOfBirth','spouseEmploymentOther',
        'fatherRace','spouseOccupation','fatherRaceOther','spouseInvolved','fatherEthnicity',
        'homeLanguages','oftenEnglish','motherDOB','motherCityOfBirth','motherRace','motherRaceOther',
        'motherEthnicity','progress','email','kID','yourRelation','yourRelationOther','yourDOB',
        'yourCityOfBirth','yourRace','yourRaceSpecify','yourEthnicity','educationLevel','maritalStatus',
        'yourEmploymentStatus','yourEmploymentOther','yourOccupation','householdIncome','zipCode',
        'liveWithSpouse','timestamp','ip'])

# Load into dataframes
data1 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)
data2 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)

isSame_parent_info = data1.equals(data2)

###############
# FAMILY INFO #
###############
   
# Specify input CSV files
inFile1 = "/Users/wayne/babysleep/test_dump/webform_views_family_info20160515060010.csv"
inFile2 = "/Users/wayne/babysleep/backup_5_5_16/webform_views_family_info20160505180005.csv"

# Specify header organization
hdr = (['sID', 'uID', 'f1FirstName', 'f2FirstName', 'f3FirstName','f4FirstName', 'f5FirstName', 
        'f6FirstName','f7FirstName','f8FirstName','f9FirstName','f1MiddleInitial','f2MiddleInitial',
        'f3MiddleInitial', 'f4MiddleInitial','f5MiddleInitial', 'f6MiddleInitial','f7MiddleInitial',
        'f8MiddleInitial','f9MiddleInitial','f1DOB','f2DOB','f3DOB','f4DOB','f5DOB','f6DOB',
        'f7DOB','f8DOB','f9DOB','f1Gender','f2Gender','f3Gender','f4Gender','f5Gender',
        'f6Gender','f7Gender','f8Gender','f9Gender','f1Relation','f2Relation','f3Relation',
        'f4Relation','f5Relation','f6Relation','f7Relation','f8Relation','f9Relation','f1Diagnosis',
        'f2Diagnosis','f3Diagnosis','f4Diagnosis','f5Diagnosis','f6Diagnosis','f7Diagnosis',
        'f8Diagnosis','f9Diagnosis','f1AddFamily','f2AddFamily','f3AddFamily','f4AddFamily','f5AddFamily',
        'f6AddFamily','f7AddFamily','f8AddFamily','progress','email','kID',
        'babyFamilyDiagnosed','timeStamp','ip'])

# Load into dataframes
data1 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)
data2 = pd.read_csv(inFile1, header=0, names=hdr, error_bad_lines=False)

isSame_family_info = data1.equals(data2)