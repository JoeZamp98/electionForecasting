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

presPercent_party_pivoted_20 = presPercent_pivoted.pivot_table(index=['state', 'county_name', 'mode'], columns=['party'], values='2020', aggfunc='mean')

for column in presPercent_party_pivoted_20.columns:

    presPercent_party_pivoted_20.rename(columns={column: column + '_20'}, inplace=True)

presPercent_party_pivoted_16 = presPercent_pivoted.pivot_table(index=['state', 'county_name', 'mode'], columns=['party'], values='2016', aggfunc='mean')

for column in presPercent_party_pivoted_16.columns:

    presPercent_party_pivoted_16.rename(columns={column: column + '_16'}, inplace=True)


presPercent_party_pivoted_12 = presPercent_pivoted.pivot_table(index=['state', 'county_name', 'mode'], columns=['party'], values='2012', aggfunc='mean')

for column in presPercent_party_pivoted_12.columns:

    presPercent_party_pivoted_12.rename(columns={column: column + '_12'}, inplace=True)

pres_mergedFullPivot = pd.merge(presPercent_party_pivoted_20, presPercent_party_pivoted_16, how='inner', left_index=True, right_index=True)

pres_mergedFullPivot = pd.merge(pres_mergedFullPivot, presPercent_party_pivoted_12, how='inner', left_index=True, right_index=True)

pres_mergedFullPivot.reset_index(inplace=True)

def determine_victory(row, year):

    if row['REPUBLICAN_' + year] > row['DEMOCRAT_' + year]:

        return "Republican"
    
    elif row['REPUBLICAN_' + year] < row['DEMOCRAT_' + year]:

        return "Democrat"
    
    else:

        return "Other"
    
relevant_years = ['12', '16', '20']

for year in relevant_years:

    pres_mergedFullPivot['Victor_' + year] = pres_mergedFullPivot.apply(determine_victory,  args=(year,), axis=1)

    pres_mergedFullPivot['Margin_' + year] = (pres_mergedFullPivot['REPUBLICAN_' + year] - pres_mergedFullPivot['DEMOCRAT_' + year])

pres_mergedFullPivot['Swing_12_16'] = pres_mergedFullPivot['Margin_16'] - pres_mergedFullPivot['Margin_12']


pres_mergedFullPivot['Swing_16_20'] = pres_mergedFullPivot['Margin_20'] - pres_mergedFullPivot['Margin_16']


## -- Read In Population Data -- ##

population_data_raw = pd.read_excel('../sourceData/populationData_2020_2022.xlsx')

population_data_raw.columns = ['Location', 'April2020', 'July2020', 'July2021', 'July2022']

population_data_raw = population_data_raw[4:-5]

population_data_raw['Location'] = population_data_raw['Location'].replace(['\.', ' County', ' Parish'], '', regex=True).str.strip().str.upper()

population_data_raw[['County', 'State']] = population_data_raw['Location'].str.split(',', expand=True)

population_data_raw['percentChange'] = (population_data_raw['July2022'] / population_data_raw['July2020']) - 1

