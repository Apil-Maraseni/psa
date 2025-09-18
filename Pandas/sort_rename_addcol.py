import pandas as pd
#we can sort a DataFrame by a specific column by using .sort_values():
#we can rename a column to another using .rename().
#we can also add column.

#its example is as follows:

# App data
app_data = {
  'app_name': [
    'YouTube', 'TikTok', 'Instagram', 'Spotify', 'Duolingo', 
    'Twitter', 'Headspace', 'Discord', 'Depop'
  ],
  'category': [
    'Video', 'Social Media', 'Social Media', 'Music', 'Education',
    'Social Media', 'Health', 'Communication', 'Shopping'
  ],
  'rating': [
    4.7, 4.6, 4.5, 4.6, 4.7,
    4.3, None, 4.7, 4.4
  ],
  'downloads_millions': [
    5000, 3000, 3500, 2000, None,
    1500, 500, 600, 200
  ]
}

# Create the DataFrame
apps = pd.DataFrame(app_data)

#Adding a column downloaded
apps['downloaded'] = [
    True,
    True,
    True,
    False,
    False,
    True,
    True,
    False,
    False
]
print(apps)

#sorting the apps by rating so that highest rated apps are at the top of the DataFrame
sorting = apps.sort_values(by = 'rating', ascending = False)
print(sorting)

#renaming a column 
apps = apps.rename(columns={'app_name':'name'})
print(apps)


