import pandas as pd
import xlrd as xl

'''This is here just so that I don't have to run the conversion python file just to test smaller things but I'll probably move it over at some point'''
'''or reference this file if it gets large enough. I think I might actually prefer having them seperated for my sanity's sake.'''

data = pd.read_csv('S:\Energy\Database Progress\CleanedWorksheets\SERC-Main Electric Device 3.csv')

#print(data)

data1 = pd.melt(data, id_vars=["Date_Time", "ID", "TF Bldg"], var_name='meter_boxes', value_name='kW')

#print(data1)

data1.to_csv(r'S:\Energy\Database Progress\CleanedWorksheets\test.csv', index=False)

data2 = pd.read_csv('S:\Energy\Database Progress\CleanedWorksheets\SERC-Stm and CHW Bldg Device 4.csv')

print(data2)
data2.to_csv(r'S:\Energy\Database Progress\CleanedWorksheets\beforeconvertingdata2.csv', index=False)
'''So before melting the columns into the correct order ("Date_Time", "ID", "TF Bldg", "kW"), you decided it made more sense to make adjustments to the columns as the were currently formatted before that'''
'''What this means is, you can just go through the columns and change them to represent the value in that unit as it should be by default (which is kW)'''
'''Later you'll go back in and add other units of measurement but for now kW is the wave'''
'''Because you'll have them rearranged after this step, it's possible you'll have to sift through the meter_boxes column to get the unit you actually need'''
for column in data2:
    if 'kBtu' in column:
        data2[column] = data2[column].divide(3.412)
    if 'Lb/hr' in column:
        data2[column] = data2[column].multiply(.305)
    if 'KBtu/Min' in column:
        data2[column] = data2[column].multiply(17.584)



print(data2)

data3 = pd.melt(data2, id_vars=["Date_Time", "ID", "TF Bldg"], var_name='meter_boxes', value_name='kW')

#print(data3)
data2.to_csv(r'S:\Energy\Database Progress\CleanedWorksheets\afterconvertingdata2.csv', index=False)
data3.to_csv(r'S:\Energy\Database Progress\CleanedWorksheets\test2.csv', index=False)