# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:08:51 2016

@author: wayne
"""
# TO DO: Clean up web data.
# Get rid of apostrophes
# Turn '' to Null

import sqlite3
import pandas as pd
import numpy as np

########################################
# ------------------------------------ #
# WEB DATA --------------------------- #
# ------------------------------------ #
########################################

# set up web data tables
# from baby info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/code/ParticipantDataDumps/webform_views_baby_info20160718060018.csv"

# load csv
hdr = (['rID','sID', 'uID', 'birthOrder', 'ofTotalBorn','deleteMe','pounds', 'ounces', 
        'within2Weeks','weeksEarly','weeksLate','progress','email','kID','kidRace', 'specifyRace',
        'ethnicity','birthCity','seriousInjury','describeInjury','earInfection',
        'timeSinceEarInfection','hearingLoss','describeHearingLoss',
        'whereSleep','developmentalDisorder','specifyDevelopmentalDisorder',
        'specifyOtherDisorder','timeStamp','ip'])
baby_info_table = pd.read_csv(inFile, header=0, names=hdr,error_bad_lines=False,quotechar='\'')
baby_info_table = baby_info_table.replace({"''":np.nan},regex=True)
baby_info_table = baby_info_table.replace({"'":""},regex=True)

# from sibling info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/code/ParticipantDataDumps/webform_views_biological_sibling_info20160718060019.csv"

# load csv
hdr = (['rID', 'sID', 'uID', 'bs1FirstName', 'bs2FirstName', 'bs3FirstName','bs4FirstName', 'bs5FirstName', 
        'bs6FirstName','bs7FirstName','bs8FirstName','bs9FirstName','bs1MiddleInitial','bs2MiddleInitial',
        'bs3MiddleInitial', 'bs4MiddleInitial','bs5MiddleInitial', 'bs6MiddleInitial','bs7MiddleInitial',
        'bs8MiddleInitial','bs9MiddleInitial','bs1DOB','bs2DOB','bs3DOB','bs4DOB','bs5DOB','bs6DOB',
        'bs7DOB','bs8DOB','bs9DOB','bs1Gender','bs2Gender','bs3Gender','bs4Gender','bs5Gender',
        'bs6Gender','bs7Gender','bs8Gender','bs9Gender','bs1AddSibling','bs2AddSibling','bs3AddSibling',
        'bs4AddSibling','bs5AddSibling','bs6AddSibling','bs7AddSibling','bs8AddSibling','bs9AddSibling',
        'email','kID','anySiblings','timeStamp','ip'])
sibling_info_table = pd.read_csv(inFile, header=0, names=hdr,error_bad_lines=False,quotechar='\'')
sibling_info_table = sibling_info_table.replace({"''":np.nan},regex=True)
sibling_info_table = sibling_info_table.replace({"'":""},regex=True)

# from diagnosis info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/code/ParticipantDataDumps/webform_views_child_diagnosis20160718060024.csv"

# load csv
hdr = ['rID','sID', 'uID', 'email', 'kID', 'diagnosis','other', 'timestamp','ip'] 
diagnosis_info_table = pd.read_csv(inFile, header=0, names=hdr,error_bad_lines=False,quotechar='\'')
diagnosis_info_table = diagnosis_info_table.replace({"''":np.nan},regex=True)
diagnosis_info_table = diagnosis_info_table.replace({"'":""},regex=True)

# from register info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/code/ParticipantDataDumps/webform_views_register_your_baby_for_the_research_study20160718060016.csv"

# load csv
hdr = (['rID','sID', 'uID', 'instructions', 'instructions1', 'instructions2','instructions3', 'email', 
        'kID','instructionsKid','DOB','gender','firstName','middleInitial','instructions4',
        'instructions5','instructions6','timeStamp','ip'])
register_info_data = pd.read_csv(inFile, header=0, names=hdr,error_bad_lines=False,quotechar='\'')

# Now let's trim useless columns and create tables
register_info_table = register_info_data.drop('instructions',axis=1)
register_info_table = register_info_table.drop('instructions1',axis=1)
register_info_table = register_info_table.drop('instructions2',axis=1)
register_info_table = register_info_table.drop('instructions3',axis=1)
register_info_table = register_info_table.drop('instructions4',axis=1)
register_info_table = register_info_table.drop('instructions5',axis=1)
register_info_table = register_info_table.drop('instructions6',axis=1)
register_info_table['DOB'] = pd.to_datetime(register_info_table['DOB'],errors='coerce')
register_info_table = register_info_table.replace({"''":np.nan},regex=True)
register_info_table = register_info_table.replace({"'":""},regex=True)

# from parent info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/code/ParticipantDataDumps/webform_views_parent_info20160718060024.csv"

# load csv
hdr = (['rID', 'sID','uID','numAdults','numChildren','spouseRelationship','spouseRelationshipOther',
        'spouseDOB','fatherDOB','spouseEmploymentStatus','fatherCityOfBirth','spouseEmploymentOther',
        'fatherRace','spouseOccupation','fatherRaceOther','spouseInvolved','fatherEthnicity',
        'homeLanguages','oftenEnglish','motherDOB','motherCityOfBirth','motherRace','motherRaceOther',
        'motherEthnicity','progress','email','kID','yourRelation','yourRelationOther','yourDOB',
        'yourCityOfBirth','yourRace','yourRaceSpecify','yourEthnicity','educationLevel','maritalStatus',
        'yourEmploymentStatus','yourEmploymentOther','yourOccupation','householdIncome','zipCode',
        'liveWithSpouse','timestamp','ip'])
parent_info_data = pd.read_csv(inFile, header=0, names=hdr,error_bad_lines=False,quotechar='\'')

# Now let's trim useless columns and create tables
parent_info_table = parent_info_data.drop('progress',axis=1)
parent_info_table = parent_info_table.replace({"''":np.nan},regex=True)
parent_info_table = parent_info_table.replace({"'":""},regex=True)

# from family info web dump
# setup io file names
inFile = "/Users/wayne/babysleep/code/ParticipantDataDumps/webform_views_family_info20160718060019.csv"

# load csv
hdr = (['rID','sID', 'uID', 'f1FirstName', 'f2FirstName', 'f3FirstName','f4FirstName', 'f5FirstName', 
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
family_info_data = pd.read_csv(inFile, header=0, names=hdr,error_bad_lines=False,quotechar='\'')

# Now let's trim useless columns and create tables
family_info_table = family_info_data.drop('progress',axis=1)
family_info_table = family_info_table.replace({"''":np.nan},regex=True)
family_info_table = family_info_table.replace({"'":""},regex=True)

########################################
# ------------------------------------ #
# APP DATA --------------------------- #
# ------------------------------------ #
########################################

# setup io file names for app data
inFile = "/Users/wayne/babysleep/code/WebDumps/clean_all.csv"

# load app data csv
hdr = ['kidID', 'entryID', 'startTime', 'endTime', 'activity','durationMin','quantity','extraData','text','notes','caregiver','childName']
data = pd.read_csv(inFile, header=0, names=hdr)
data.startTime = pd.to_datetime(data.startTime, errors='coerce')
data.endTime = pd.to_datetime(data.endTime, errors='coerce')

# calculate and add age at time each event was logged
k_dob = []
register_info_table.kID = pd.to_numeric(register_info_table.kID,errors='coerce')

for row in data.kidID:
    m = register_info_table[register_info_table.kID==row]
    if len(m) == 0:
        k_dob.append('Not Found')
    else:            
        e = register_info_table[register_info_table.kID==row].index[0]
        k_dob.append(register_info_table.DOB[e])
        
k_dob = pd.Series(k_dob)
k_dob = pd.to_datetime(k_dob, errors='coerce')
wem=pd.Series(data.startTime).copy()
wem=wem.reset_index(drop=True)
x=wem-k_dob
x=x.dt.days
data['daysOld'] = x.copy()

# segment our app data into tables
kIDs = {'kID':pd.unique(data.kidID.ravel())}
kid_table = pd.DataFrame(kIDs)
entry_table = data[['entryID','activity','kidID']]
sleep_table = data[(data['activity'] == "Sleep")]
diaper_table = data[(data['activity'] == "Diaper")]
mood_table = data[(data['activity'] == "Mood")]
milestone_table = data[(data['activity'] == "Milestone")]
nursing_table = data[(data['activity'] == "Nursing")]
weight_table = data[(data['activity'] == "Weight")]
diary_table = data[(data['activity'] == "Diary")]
health_table = data[(data['activity'] == "Health")]
height_table = data[(data['activity'] == "Height")]
headsize_table = data[(data['activity'] == "Head Size")]
activity_table = data[(data['activity'] == "Activity")]
bottle_table = data[(data['activity'] == "Bottle")]
expressed_table = data[(data['activity'] == "Expressed")]
solidfood_table = data[(data['activity'] == "Solid Food")]
message_table = data[(data['activity'] == "Message")]
medicine_table = data[(data['activity'] == "Medicine")]
temperature_table = data[(data['activity'] == "Temperature")]
potty_table = data[(data['activity'] == "Potty")]
sleepstart_table = data[(data['activity'] == "Sleep Start")]

# Drop columns we don't need in certain tables
# Delete activity column
sleep_table = sleep_table.drop('activity',axis=1)
diaper_table = diaper_table.drop('activity',axis=1)
mood_table = mood_table.drop('activity',axis=1)
milestone_table = milestone_table.drop('activity',axis=1)
nursing_table = nursing_table.drop('activity',axis=1)
weight_table = weight_table.drop('activity',axis=1)
diary_table = diary_table.drop('activity',axis=1)
health_table = health_table.drop('activity',axis=1)
headsize_table = headsize_table.drop('activity',axis=1)
activity_table = activity_table.drop('activity',axis=1)
bottle_table = bottle_table.drop('activity',axis=1)
expressed_table = expressed_table.drop('activity',axis=1)
solidfood_table = solidfood_table.drop('activity',axis=1)
message_table = message_table.drop('activity',axis=1)
medicine_table = medicine_table.drop('activity',axis=1)
temperature_table = temperature_table.drop('activity',axis=1)
potty_table = potty_table.drop('activity',axis=1)
sleepstart_table = sleepstart_table.drop('activity',axis=1)

# Drop from diary table
diary_table = diary_table.drop('durationMin',axis=1)
diary_table = diary_table.drop('quantity',axis=1)
diary_table = diary_table.drop('extraData',axis=1)

# Drop from diaper table
diaper_table = diaper_table.drop('durationMin',axis=1)

# Drop from headsize table
headsize_table = headsize_table.drop('durationMin',axis=1)

# Drop from health table
health_table = health_table.drop('durationMin',axis=1)
health_table = health_table.drop('quantity',axis=1)

# Drop from height table
height_table = height_table.drop('durationMin',axis=1)

# Drop from medicine table
medicine_table = medicine_table.drop('durationMin',axis=1)

# Drop from message table
message_table = message_table.drop('durationMin',axis=1)
message_table = message_table.drop('quantity',axis=1)
message_table = message_table.drop('extraData',axis=1)
message_table = message_table.drop('notes',axis=1)

# Drop from nursing table
nursing_table = nursing_table.drop('quantity',axis=1)

# Drop from sleep table
sleep_table = sleep_table.drop('quantity',axis=1)

# Drop from sleepstart table
sleepstart_table = sleepstart_table.drop('durationMin',axis=1)
sleepstart_table = sleepstart_table.drop('quantity',axis=1)
sleepstart_table = sleepstart_table.drop('extraData',axis=1)

# Drop from temperature table
temperature = temperature_table.drop('durationMin',axis=1)
temperature = temperature_table.drop('quantity',axis=1)

# Drop from weight table
weight_table = weight_table.drop('durationMin',axis=1)

# create new db and make connection
conn = sqlite3.connect('babysleep.db')
conn.text_factory = str

# write tables WEB
baby_info_table.to_sql(con=conn, name='Baby_Info', if_exists='replace', flavor='sqlite', index=False)
diagnosis_info_table.to_sql(con=conn, name='Diagnosis_Info', if_exists='replace', flavor='sqlite', index=False)
family_info_table.to_sql(con=conn, name='Family_Info', if_exists='replace', flavor='sqlite', index=False)
parent_info_table.to_sql(con=conn, name='Parent_Info', if_exists='replace', flavor='sqlite', index=False)
register_info_table.to_sql(con=conn, name='Register_Info', if_exists='replace', flavor='sqlite', index=False)
sibling_info_table.to_sql(con=conn, name='Sibling_Info', if_exists='replace', flavor='sqlite', index=False)

# write tables APP
kid_table.to_sql(con=conn, name='Kids', if_exists='replace', flavor='sqlite', index=False)
entry_table.to_sql(con=conn, name='Entries', if_exists='replace', flavor='sqlite', index=False)
sleep_table.to_sql(con=conn, name='Sleep', if_exists='replace', flavor='sqlite', index=False)
diaper_table.to_sql(con=conn, name='Diaper', if_exists='replace', flavor='sqlite', index=False)
mood_table.to_sql(con=conn, name='Mood', if_exists='replace', flavor='sqlite', index=False)
milestone_table.to_sql(con=conn, name='Milestone', if_exists='replace', flavor='sqlite', index=False)
nursing_table.to_sql(con=conn, name='Nursing', if_exists='replace', flavor='sqlite', index=False)
weight_table.to_sql(con=conn, name='Weight', if_exists='replace', flavor='sqlite', index=False)
diary_table.to_sql(con=conn, name='Diary', if_exists='replace', flavor='sqlite', index=False)
health_table.to_sql(con=conn, name='Health', if_exists='replace', flavor='sqlite', index=False)
height_table.to_sql(con=conn, name='Height', if_exists='replace', flavor='sqlite', index=False)
headsize_table.to_sql(con=conn, name='Head_Size', if_exists='replace', flavor='sqlite', index=False)
activity_table.to_sql(con=conn, name='Activity', if_exists='replace', flavor='sqlite', index=False)
bottle_table.to_sql(con=conn, name='Bottle', if_exists='replace', flavor='sqlite', index=False)
expressed_table.to_sql(con=conn, name='Expressed', if_exists='replace', flavor='sqlite', index=False)
solidfood_table.to_sql(con=conn, name='Solid_Food', if_exists='replace', flavor='sqlite', index=False)
message_table.to_sql(con=conn, name='Message', if_exists='replace', flavor='sqlite', index=False)
medicine_table.to_sql(con=conn, name='Medicine', if_exists='replace', flavor='sqlite', index=False)
temperature_table.to_sql(con=conn, name='Temperature', if_exists='replace', flavor='sqlite', index=False)
potty_table.to_sql(con=conn, name='Potty', if_exists='replace', flavor='sqlite', index=False)
sleepstart_table.to_sql(con=conn, name='Sleep_Start', if_exists='replace', flavor='sqlite', index=False)

# close connection
conn.close()

# create CSV files for MATLAB import
# write tables WEB
baby_info_table.to_csv('baby_info.csv',sep='\t')
diagnosis_info_table.to_csv('diagnosis_info.csv',sep='\t')
family_info_table.to_csv('family_info.csv',sep='\t')
parent_info_table.to_csv('parent_info.csv',sep='\t')
register_info_table.to_csv('register_info.csv',sep='\t')
sibling_info_table.to_csv('sibling_info.csv',sep='\t')

# write tables APP
kid_table.to_csv('kid_table.csv',sep='\t')
entry_table.to_csv('entry_table.csv',sep='\t')
sleep_table.to_csv('sleep_table.csv',sep='\t')
diaper_table.to_csv('diaper_table.csv',sep='\t')
mood_table.to_csv('mood_table.csv',sep='\t')
milestone_table.to_csv('milestone_table.csv',sep='\t')
nursing_table.to_csv('nursing_table.csv',sep='\t')
weight_table.to_csv('weight_table.csv',sep='\t')
diary_table.to_csv('diary_table.csv',sep='\t')
health_table.to_csv('health_table.csv',sep='\t')
height_table.to_csv('height_table.csv',sep='\t')
headsize_table.to_csv('headsize_table.csv',sep='\t')
activity_table.to_csv('activity_table.csv',sep='\t')
bottle_table.to_csv('bottle_table.csv',sep='\t')
expressed_table.to_csv('expressed_table.csv',sep='\t')
solidfood_table.to_csv('solidfood_table.csv',sep='\t')
message_table.to_csv('message_table.csv',sep='\t')
medicine_table.to_csv('medicine_table.csv',sep='\t')
temperature_table.to_csv('temperature_table.csv',sep='\t')
potty_table.to_csv('potty_table.csv',sep='\t')
sleepstart_table.to_csv('sleepstart_table.csv',sep='\t')

#k_dob = []
#
#for row in kid_table['kID']:
#    e = register_info_table['DOB'][register_info_table['kID'] == row]
#    e = e.tolist()
#    k_dob.append(e)
#
#print 'done'

#for x in range(len(kid_table['kID'])):
#    e = register_info_table.loc[register_info_table['kID'] == kid_table['kID'][x]]
#    k_dob.append(e['DOB'].astype(str))
#    
#print 'done'