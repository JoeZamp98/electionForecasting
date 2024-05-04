import numpy as np
import pandas as pd

## -- Exploring Data / Calculting Percentage Results -- ##

pres_allRecords = pd.read_csv('../sourceData/countypres_2000-2020.csv')

pres_allRecords['percentOfTotal'] = pres_allRecords['candidatevotes'] / pres_allRecords['totalvotes']

print(pres_allRecords['mode'].unique())

pres_earlyVote = pres_allRecords[pres_allRecords['mode'].isin(['EARLY VOTE', 'EARLY VOTING', 'EARLY', 'MAIL', 'ABSENTEE', 'IN-PERSON ABSENTEE', '2ND ABSENTEE'])]

pres_electionDay = pres_allRecords[pres_allRecords['mode'] == 'ELECTION DAY']

print(pres_allRecords['state'].unique())

battlegrounds = ['FLORIDA', 'GEORGIA', 'IOWA', 'MAINE', 'MICHIGAN', 'NEVADA', 'NEW HAMPSHIRE', 'NORTH CAROLINA', 'OHIO', 'PENNSYLVANIA', 'WISCONSIN']

