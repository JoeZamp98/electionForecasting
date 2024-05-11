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

print(pres_allRecords['party'].unique())

pres_allRecords = pres_allRecords[~pres_allRecords.index.duplicated()]

pres_allRecords.reset_index(inplace=True)

pres_allRecords['year'].replace({
    2000: '2000',
    2004: '2004',
    2008: '2008',
    2012: '2012',
    2016: '2016',
    2020: '2020'
}, inplace=True)


presPercent_pivoted = pres_allRecords.pivot_table(index=['state', 'county_name', 'party', 'mode'], columns=['year'], values='percentOfTotal', aggfunc='mean')


presPercent_pivoted = presPercent_pivoted[(pd.isna(presPercent_pivoted['2012']) == False) & (pd.isna(presPercent_pivoted['2016']) == False) & (pd.isna(presPercent_pivoted['2020']) == False)]

presPercent_pivoted.reset_index(inplace=True)

presPercent_pivoted['Swing_16_20'] = presPercent_pivoted['2020'] - presPercent_pivoted['2016']

presPercent_pivoted['Swing_12_16'] = presPercent_pivoted['2016'] - presPercent_pivoted['2012']


presPercent_party_pivoted = presPercent_pivoted.pivot_table(index=['state', 'county_name', 'mode', '2012', '2016'], columns=['party'], values='2020', aggfunc='mean')

presPercent_party_pivoted.reset_index(inplace=True)

# presPercent_party_pivoted = presPercent_party_pivoted.pivot_table(index=['state', 'county_name', 'mode', '2012'], values='2016', aggfunc='mean')

# presPercent_party_pivoted.reset_index(inplace=True)

# presPercent_party_pivoted = presPercent_party_pivoted.pivot_table(index=['state', 'county_name', 'mode'], values='2012', aggfunc='mean')
