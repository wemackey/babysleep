# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:21:12 2015

@author: wayne
"""

import pandas as pd

# from app dump
# setup io file names
inFile = "/Users/wayne/Downloads/Archive/clean_merged.csv"

# load csv
hdr = ['kidID', 'entryID', 'startTime', 'endTime', 'activity','durationMin','quantity','extraData','text','notes','caregiver','childName']
data = pd.read_csv(inFile, header=0, names=hdr)

# from baby info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/db/webform_views_baby_info20160130120006_fixed.csv"

# load csv
hdr = (['sID', 'uID', 'birthOrder', 'ofTotalBorn', 'del_me','pounds', 'ounces', 
        'within2Weeks','weeksEarly','weeksLate','progress','email','kID','kidRace', 'specifyRace',
        'ethnicity','birthCity','seriousInjury','describeInjury','earInfection',
        'timeSinceEarInfection','hearingLoss','describeHearingLoss','timeStamp','ip'])
baby_info_data = pd.read_csv(inFile, header=0, names=hdr)

# from sibling info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/db/webform_views_biological_sibling_info20160130120006_fixed.csv"

# load csv
hdr = (['sID', 'uID', 'bs1FirstName', 'bs2FirstName', 'bs3FirstName','bs4FirstName', 'bs5FirstName', 
        'bs6FirstName','bs7FirstName','bs8FirstName','bs9FirstName','bs1MiddleInitial','bs2MiddleInitial',
        'bs3MiddleInitial', 'bs4MiddleInitial','bs5MiddleInitial', 'bs6MiddleInitial','bs7MiddleInitial',
        'bs8MiddleInitial','bs9MiddleInitial','bs1DOB','bs2DOB','bs3DOB','bs4DOB','bs5DOB','bs6DOB',
        'bs7DOB','bs8DOB','bs9DOB','bs1Gender','bs2Gender','bs3Gender','bs4Gender','bs5Gender',
        'bs6Gender','bs7Gender','bs8Gender','bs9Gender','bs1AddSibling','bs2AddSibling','bs3AddSibling',
        'bs4AddSibling','bs5AddSibling','bs6AddSibling','bs7AddSibling','bs8AddSibling','bs9AddSibling',
        'email','kID','anySiblings','timeStamp','ip'])
sibling_info_data = pd.read_csv(inFile, header=0, names=hdr)

# from diagnosis info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/db/webform_views_child_diagnosis20160130120006_fixed.csv"

# load csv
hdr = ['sID', 'uID', 'email', 'kID', 'diagnosis','other', 'timestamp','ip'] 
diagnosis_info_data = pd.read_csv(inFile, header=0, names=hdr)

# from register info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/db/webform_views_register_your_baby_for_the_research_study20160130120006_fixed.csv"

# load csv
hdr = (['sID', 'uID', 'instructions', 'instructions1', 'instructions2','instructions3', 'email', 
        'kID','instructionsKid','DOB','gender','firstName','middleInitial','instructions4',
        'instructions5','instructions6','timeStamp','ip'])
register_info_data = pd.read_csv(inFile, header=0, names=hdr)

# from parent info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/db/webform_views_parent_info20160130120006_fixed.csv"

# load csv
hdr = (['sID','uID','numAdults','numChildren','spouseRelationship','spouseRelationshipOther',
        'spouseDOB','fatherDOB','spouseEmploymentStatus','fatherCityOfBirth','spouseEmploymentOther',
        'fatherRace','spouseOccupation','fatherRaceOther','spouseInvolved','fatherEthnicity',
        'homeLanguages','oftenEnglish','motherDOB','motherCityOfBirth','motherRace','motherRaceOther',
        'motherEthnicity','progress','email','kID','yourRelation','yourRelationOther','yourDOB',
        'yourCityOfBirth','yourRace','yourRaceSpecify','yourEthnicity','educationLevel','maritalStatus',
        'yourEmploymentStatus','yourEmploymentOther','yourOccupation','householdIncome','zipCode',
        'liveWithSpouse','timestamp','ip'])
parent_info_data = pd.read_csv(inFile, header=0, names=hdr)

# from family info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/db/webform_views_family_info20160130120006_fixed.csv"

# load csv
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
family_info_data = pd.read_csv(inFile, header=0, names=hdr)