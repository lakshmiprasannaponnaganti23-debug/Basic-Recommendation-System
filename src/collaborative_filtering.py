import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")


# Create user-item matrix
user_item_matrix = ratings.pivot_table(
    index="userId",
    columns="movieId",
    values="rating"
)


# Replace missing ratings with 0
user_item_matrix_filled = user_item_matrix.fillna(0)


# Calculate movie-to-movie similarity
movie_similarity = cosine_similarity(
    user_item_matrix_filled.T
)


# Create similarity DataFrame
movie_similarity_df = pd.DataFrame(
    movie_similarity,
    index=user_item_matrix.columns,
    columns=user_item_matrix.columns
)


def recommend_movies(movie_title, number_of_recommendations=5):

    # Find selected movie
    matching_movies = movies[
        movies["title"].str.lower() == movie_title.lower()
    ]

    if matching_movies.empty:
        print(f"\nMovie '{movie_title}' was not found.")
        return

    selected_movie_id = matching_movies.iloc[0]["movieId"]

    # Get similarity scores
    similarity_scores = movie_similarity_df[
        selected_movie_id
    ]

    # Sort similarity scores
    similar_movie_ids = similarity_scores.sort_values(
        ascending=False
    ).index.tolist()

    # Remove selected movie
    similar_movie_ids.remove(selected_movie_id)

    # Select top movies
    top_movie_ids = similar_movie_ids[
        :number_of_recommendations
    ]

    # Get movie details
    recommended_movies = movies[
        movies["movieId"].isin(top_movie_ids)
    ]

    print(
        f"\n===== RECOMMENDATIONS FOR "
        f"{movie_title} ====="
    )

    print("-" * 70)

    for number, (_, movie) in enumerate(
        recommended_movies.iterrows(),
        start=1
    ):
        print(
            f"{number}. {movie['title']} | "
            f"Genres: {movie['genres']}"
        )


# Test
recommend_movies("Toy Story (1995)")