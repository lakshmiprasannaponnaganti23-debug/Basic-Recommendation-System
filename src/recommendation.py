import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load movie dataset
movies = pd.read_csv("data/movies.csv")

# Fill missing genres
movies["genres"] = movies["genres"].fillna("")

# Convert movie genres into numerical features
vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split("|"), token_pattern=None)

genre_matrix = vectorizer.fit_transform(movies["genres"])

# Calculate similarity between all movies
similarity_matrix = cosine_similarity(genre_matrix)


def recommend_movies(movie_title, number_of_recommendations=5):
    # Find the selected movie
    matching_movies = movies[
        movies["title"].str.lower() == movie_title.lower()
    ]

    if matching_movies.empty:
        print(f"\nMovie '{movie_title}' was not found.")
        return

    movie_index = matching_movies.index[0]

    # Get similarity scores for the selected movie
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    # Sort movies by similarity score
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Select top recommendations
    recommended_movies = []

    for index, score in similarity_scores[1:]:
        recommended_movies.append(
            (movies.iloc[index]["title"], score)
        )

        if len(recommended_movies) == number_of_recommendations:
            break

    print(f"\nRecommendations for: {movie_title}")
    print("-" * 50)

    for number, (title, score) in enumerate(recommended_movies, start=1):
        print(f"{number}. {title} | Similarity: {score:.2f}")


# Test the recommendation system
recommend_movies("Toy Story (1995)")