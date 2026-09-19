import pandas as pd

# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Display basic information
print("\n===== MOVIES DATASET =====")
print(movies.head())
print("\nNumber of movies:", len(movies))
print("\nMovie columns:")
print(movies.columns.tolist())

print("\n===== RATINGS DATASET =====")
print(ratings.head())
print("\nNumber of ratings:", len(ratings))
print("\nRatings columns:")
print(ratings.columns.tolist())

# Check missing values
print("\n===== MISSING VALUES =====")
print("\nMovies:")
print(movies.isnull().sum())

print("\nRatings:")
print(ratings.isnull().sum())

# Display rating statistics
print("\n===== RATING STATISTICS =====")
print(ratings["rating"].describe())

# Display most-rated movies
rating_counts = ratings.groupby("movieId").size().sort_values(ascending=False)

print("\n===== MOST RATED MOVIES =====")
print(rating_counts.head(10))

print("\nDataset exploration completed successfully.")