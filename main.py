import pandas as pd

df1_original = pd.read_csv('/Users/ryanprince/Desktop/Projects/Combine-Reports/Hills Pet - 2022 PD Handraiser.csv')
df3_original = pd.read_csv('/Users/ryanprince/Desktop/Projects/Combine-Reports/1381146_Hills_Pet_-_2022_PD_Handraiser_20221001_031153_3858949580.csv')

# filter data by two conditions
# print(df1.loc[(df1['Placement'] == 'P1W6PT2_HLN_PD_018_Content - Custom_CLUEP_Derm Cat 300x250_Run of Network_Demo_P25+_300 x 250_Standard_Other_NA') & (df1['Total Cost'] > )])

# copy the original dataframes
df1 = df1_original.copy()
df3 = df3_original.copy()

# update first party report 
# remove dollar sign and commas from values in 'Total Cost' column
df1['Total Cost'] = df1['Total Cost'].str.replace('$', '', regex=True).str.replace(',', '', regex=True)

# change values in 'Total Cost' from string (object) to float
df1['Total Cost'] = df1['Total Cost'].astype(float)

# remove percent sign from values in 'CTR' column
df1['CTR'] = df1['CTR'].str.replace('%', '')

# change values in 'CTR' from string (object) to float
df1['CTR'] = df1['CTR'].astype(float)

# change values in 'CTR' to true decimal form by dividing by 100
df1['CTR'] = df1['CTR']/100

# get list of unique dates
# unique_dates = df1.Date.unique()

# get sum of impressions, sum of clicks, avg CTR, and sum cost by placement
df1 = df1.groupby(['Placement'], as_index=False).agg(SumImpressions=('Impressions', 'sum'),
                                                        SumClicks=('Clicks', 'sum'),
                                                        AvgCTR=('CTR', 'mean'),
                                                        SumSpend=('Total Cost', 'sum'))


# update third party (DCM) report
# change values in 'Click Rate' to true decimal amount by dividing by 100
df3['Click Rate'] = df3['Click Rate']/100

# add new calculated column 'Spend' 
df3 = df3.assign(Spend = df3['Impressions'] / 1000 * df3['CPM'])

# get sum of impressions, sum of clicks, avg CTR, and sum cost by placement
df3 = df3.groupby(['Placement'], as_index=False).agg(DCM_SumImpressions=('Impressions', 'sum'),
                                                        DCM_SumClicks=('Clicks', 'sum'),
                                                        DCM_AvgCTR=('Click Rate', 'mean'),
                                                        DCM_SumSpend=('Spend', 'sum'))


# merge dataframes 
df_merged = pd.merge(df1, df3)

# output data to csv file
df_merged.to_csv('new_test.csv')


# df_concat = pd.concat([df1, df3], ignore_index=False)
# df_concat.to_csv('concat_test.csv')


# df_placements = pd.DataFrame(columns=['Placement', '1P_Impressions', '1P_Clicks', '1P_CTR', '1P_Spend', '3P_Impressions', '3P_Clicks', '3P_CTR', '3P_Spend'] )
# placements = ['Weight Dog', 'Weight Cat', 'Derm Dog', 'Derm Cat', 'Renal Dog', 'Renal Cat','GI Dog GIB', 'GI Cat GIB', 'Dental Dog', 'Dental Cat', 'Urinary Dog', 'Urinary Cat', 'GI Dog ID', 'GI Cat ID']



# for placement in placements:
#     impressions = 0
#     print(impressions)
#     for i in df_merged.itertuples():
        
#         if placement in i.Placement:

#             # impressions += df_merged[i.SumImpressions]
#             print(df_merged[i.SumImpressions])

# for placement in placements:
#     for index, row in df_merged.iterrows():
#         impressions = 0
#         print(impressions)
#         if placement in row['Placement']:
#             # print(row['SumImpressions'])
#             impressions += row['SumImpressions']

# sum_impressions = 0
# for i in df_merged.itertuples():
#     if 'Weight Dog' in i.Placement:
#         print(i.SumImpressions)
#         sum_impressions += i.SumImpressions

# print(sum_impressions)


# for placement in placements:
#     count_placements = 0
#     sum_impressions = 0
#     sum_clicks = 0
#     sum_ctr = 0
#     sum_spend = 0
#     if df_merged[df_merged['Placement'].str.contains(placement)]:
#         print(df_merged[df_merged['Placement'].str.contains(placement)])


# print(df_placements)

# print(df1)


# .sort_values('Placement')


# print(df1.loc[df1['Placement'].str.contains('Derm Cat')])

# print(df1.head(10))
# print(df1.dtypes)
