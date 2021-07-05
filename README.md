# Pandas-and-JSON
## Using Pandas to create a dataframe from a JSON object
The JSON object is from the ICD coded list with > 4000 entries icd coded diagnoses which were acquired from GraphCMS diagnosis Schema. The query made in GraphCMS is as shown as below:
> ### Returns all diagnoses from Diagnosis Schema
```sh
query MyQuery {
	diagnoses (first: 1000, skip : 100 , orderBy:icd10_ASC) {
		nameStd 
		icd10
	}
}
```
> Running the panda and json script will give a dataframe output as follows:
																								
|   |                                       nameStd | icd10 |
|---|----------------------------------------------:|-------|
| 0 |                                       Cholera | A00   |
| 1 | Enterohemorrhagic Escherichia coli infection  | A04.3 |
| 2 |                             Salmonella sepsis | A02.1 |
| 3 |                Typhoid and paratyphoid fevers | A01   |
| 4 |         Other bacterial intestinal infections | A04   |           
|...|                                            ...|    ...|
|4012|         Presence of other functional implants|    Z96|
|4013|     Complication of surgical and medical care|  Z96.6|
|4014|                     Presence of other devices|    Z97|
[4017 rows x 2 columns]

# step 1
> Create a virtual environment and install pandas and json using the pip installer
```sh
py -m venv env 
pip install pandas
pip install json
```
# step 2
> import json and pandas into the script
```sh
import json
import pandas as pd
from pandas.io.pytables import IndexCol
```
# step 3
> implement the script as in DiagnosisQuery.py to get a csv file with the dataframe as shown above
```sh
# open and read json file and load data using Python JSON module to make into list
with open('Diagnoses.json', 'r') as f:
    diagnosesData = json.loads (f.read()) # print (type(diagnosesData)) -> <class 'dict'>   

# get diagnoses value from data key dictionary with .get()
diagnosesJson = diagnosesData.get('data') # print (type(diagnosesData.get('data')) -> <class 'dict'>
diagnosesList = diagnosesJson.get('diagnoses') # print(type(diagnosesList)) -> -> <class 'list'>

# converts list diagnosesData into json string
jsonData = json.dumps (diagnosesList) # -> <class 'str'>

# read json into dataframe object
dfJson = pd.read_json (jsonData) # -> <class 'pandas.core.frame.DataFrame'> dataframe formed by pandas

# save dataframe object into csv
dfJson.to_csv('diagnoses.csv', index=False)
```
