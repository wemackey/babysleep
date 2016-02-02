# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:08:51 2016

@author: wayne
"""

import sqlite3
import pandas as pd

# setup io file names for app data
inFile = "/Users/wayne/Downloads/Archive/clean_merged.csv"

# load app data csv
hdr = ['kidID', 'entryID', 'startTime', 'endTime', 'activity','durationMin','quantity','extraData','text','notes','caregiver','childName']
data = pd.read_csv(inFile, header=0, names=hdr)

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

# make sure dataframe exists
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