import json
import pandas as pd
from pandas.io.pytables import IndexCol

# open and read json file and load data using Python JSON module to make into list
with open('Diagnoses.json', 'r') as f:
    diagnosesData = json.loads (f.read()) # print (type(diagnosesData)) -> <class 'dict'>   

# get diagnoses value from data key dictionary with .get()
diagnosesJson = diagnosesData.get('data') # print (type(diagnosesData.get('data')) -> <class 'dict'>
diagnosesList = diagnosesJson.get('diagnoses') # print(type(diagnosesList)) -> <class 'list'>

# converts list diagnosesData into json string
jsonData = json.dumps (diagnosesList) # -> <class 'str'>

# read json into dataframe object
dfJson = pd.read_json (jsonData) # -> <class 'pandas.core.frame.DataFrame'> dataframe formed by pandas

# save dataframe object into csv
dfJson.to_csv('diagnoses.csv', index=False)
