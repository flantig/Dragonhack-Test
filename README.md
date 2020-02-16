#DragonHack Test Readme
##Just get familiar with it, we're gonna be using it a lot 

Alright, here is the test github repo. I'm using the gui to save time since I have some experience using it over the summer. If you choose to do the gui and want to use it, it's really easy to use and cloning it using the grean dropdown on the top right works similarly to a magnet torrent. You'll get a small popup asking you if you want to use a desktop app and the rest is pretty straight forward.

If any of us decide to work on the same file for whatever reason or we commit things at the same time, we'll run into an issue where we just overwrite whatever progress we push in. In those cases you can just grab what you were working on from a previous commit and push it again.

Below is some sample code from work. Just some filler test, I'm messing around with github's readme thing.

'''
import pandas as pd
import xlrd as xl

data = pd.read_csv('S:\Energy\Database Progress\CleanedWorksheets\SERC-Main Electric Device 3.csv')

print(data)

data1 = pd.melt(data, id_vars=["Date_Time", "ID", "TF Bldg"], var_name='meter_boxes', value_name='kW')

print(data1)

data1.to_csv(r'S:\Energy\Database Progress\CleanedWorksheets\test.csv', index=False)

data2 = pd.read_csv('S:\Energy\Database Progress\CleanedWorksheets\SERC-Stm and CHW Bldg Device 4.csv')

for column in data2:
   if 'kBtu' in column:
       data2[column] = data2[column].divide(3.412)
   if 'kBtu' in column:
       data2[column] = data2[column].divide(3.412)


print(data2)

data3 = pd.melt(data2, id_vars=["Date_Time", "ID", "TF Bldg"], var_name='meter_boxes', value_name='kW')

print(data3)
data2.to_csv(r'S:\Energy\Database Progress\CleanedWorksheets\test3.csv', index=False)
data3.to_csv(r'S:\Energy\Database Progress\CleanedWorksheets\test2.csv', index=False)
'''