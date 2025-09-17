import pandas as pd

# Recent Oscar winners
movie_data = {
  'title': ['Parasite', 'Nomadland', 'CODA', 'Everything Everywhere All at Once', 'Oppenheimer', 'Anora'],
  'release_date': ['2019-05-30', '2020-09-11', '2021-01-28', '2022-03-11', '2023-07-21', '2024-05-24'],
  'genre': ['Thriller', 'Drama', 'Drama',  'Action', 'Biography', 'Drama'],
  'studio': ['CJ Entertainment', 'Searchlight Pictures', 'Apple TV+', 'A24', 'Universal Pictures', 'A24'],
  'budget': [11400000, 5000000, 10000000, 25000000, 100000000, 3000000],
  'box_office': [263000000, 39000000, 1900000, 143000000, 975000000, 57000000],
  'runtime_minutes': [132, 108, 111, 139, 180, 98],
  'rating': [8.5, 7.3, 8.0, 8.0, 8.6, 8.1]
}

# Create the DataFrame
movies = pd.DataFrame(movie_data)
