import pandas as pd

# Example data about The Weeknd's songs
weeknd_data = {
    "song": [
        "Blinding Lights", "Save Your Tears", "Starboy", "The Hills", "Can't Feel My Face",
        "Die For You", "In The Night", "After Hours", "I Feel It Coming", "Sacrifice"
    ],
    "album": [
        "After Hours", "After Hours", "Starboy", "Beauty Behind the Madness", "Beauty Behind the Madness",
        "Starboy", "Beauty Behind the Madness", "After Hours", "Starboy", "Dawn FM"
    ],
    "release_year": [
        2020, 2020, 2016, 2015, 2015,
        2016, 2015, 2020, 2016, 2022
    ],
    "streams_millions": [
        4000, 2500, 2700, 1800, 2000,
        1500, 800, 1200, 1600, 600
    ],
    "featured_artist": [
        None, None, "Daft Punk", None, None,
        None, None, None, "Daft Punk", None
    ]
}

# Create DataFrame
weeknd_df = pd.DataFrame(weeknd_data)
# print(weeknd_df)

#adding a new columns
weeknd_df['duration_time'] = [
    3.20, 3.35, 3.50, 4.02, 3.36,
    4.00, 4.39, 6.01, 4.29, 3.09
]
# print(weeknd_df)

sorting = weeknd_df.sort_values(by = 'release_year', ascending = True)
# print(sorting)

#to dispaly only the songs released after the year 2018
songs_after_2018 = weeknd_df[weeknd_df['release_year'] > 2018]
# print(songs_after_2018)

#to display only the songs with stream over 2000 million:
mills = weeknd_df[weeknd_df['streams_millions'] > 2000]
# print(mills)

#songs from starboy album and featuring draft_punk
starboy = weeknd_df[(weeknd_df["album"] == 'Starboy') & (weeknd_df['featured_artist'] == "Daft Punk")]
print(starboy)
