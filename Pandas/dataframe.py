import pandas as pd
#creawting data frame from dictionary
data = {
    'city':['Brooklyn', 'Seoul', 'Barcelona', 'Mexico City'],
    'country':['US', 'South Korea', 'Spain', 'Mexico'],
    'population':[2646000,9411000,163000,9209944]
}

df = pd.DataFrame(data)

#creating data frame from list
data = [
  ['Brooklyn', 'US', 2646000],
  ['Seoul', 'South Korea', 9411000],
  ['Barcelona', 'Spain', 1636000],
  ['Mexico City', 'Mexico', 9209944]
]

df1 = pd.DataFrame(data, columns=['city', 'country', 'population'])

#importing from a csv file
df2 = pd.read_csv('my_filename.csv')

#importing from other file types: we will need a 'delimiter' parameter
df = pd.read_csv('my_filename.tsv', delimiter='\t')

