import pandas as pd
import datetime


current_date = datetime.datetime.now()

file1 = str(current_date.year) + '-' + str(current_date.month) + '-' + str(current_date.day) + '-' + 'cnnespanol'+'.csv'
file2 = str(current_date.year) + '-' + str(current_date.month) + '-' + str(current_date.day) + '-' + 'bbcmundo'+'.csv'
file3 = str(current_date.year) + '-' + str(current_date.month) + '-' + str(current_date.day) + '-' + 'semana'+'.csv'
file4 = str(current_date.year) + '-' + str(current_date.month) + '-' + str(current_date.day) + '-' + 'eltiempo'+'.csv'

# Assuming 'file1.csv', 'file2.csv', 'file3.csv' are your csv files
df1 = pd.read_csv(file3)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file1)
df4 = pd.read_csv(file4)

# Combine dataframes
result = pd.concat([df1, df2, df3, df4])

# If you want to save the combined dataframe as a new csv file
result.to_csv('combined.csv', index=False)



print("done!")