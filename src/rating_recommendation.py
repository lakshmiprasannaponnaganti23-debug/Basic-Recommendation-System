import pandas as pd


# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")


# Calculate the average rating and number of ratings for every movie
movie_stats = ratings.groupby("movieId").agg(
    average_rating=("rating", "mean"),
    rating_count=("rating", "count")
).reset_index()


# Merge movie information with rating statistics
movie_data = movies.merge(movie_stats, on="movieId", how="inner")


# Calculate a recommendation score
# Movies with good ratings and enough ratings receive higher scores
movie_data["recommendation_score"] = (
    movie_data["average_rating"] *
    (movie_data["rating_count"] / movie_data["rating_count"].max())
)


# Sort movies by recommendation score
recommended_movies = movie_data.sort_values(
    "recommendation_score",
    ascending=False
)


print("\n===== TOP MOVIE RECOMMENDATIONS =====")
print("-" * 70)

for number, (_, movie) in enumerate(
    recommended_movies.head(10).iterrows(),
    start=1
):
    print(
        f"{number}. {movie['title']} | "
        f"Rating: {movie['average_rating']:.2f} | "
        f"Ratings: {int(movie['rating_count'])}"
    )


print("\nRecommendation system completed successfully.")