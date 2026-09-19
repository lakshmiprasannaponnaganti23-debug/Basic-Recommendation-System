import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Basic Recommendation System",
    page_icon="🎬"
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    movies = pd.read_csv("data/movies.csv")
    ratings = pd.read_csv("data/ratings.csv")

    return movies, ratings


movies, ratings = load_data()


# --------------------------------------------------
# CREATE MOVIE-USER MATRIX
# --------------------------------------------------

@st.cache_resource
def create_recommendation_model(ratings):

    movie_user_matrix = ratings.pivot_table(
        index="movieId",
        columns="userId",
        values="rating"
    )

    return movie_user_matrix


movie_user_matrix = create_recommendation_model(ratings)


# --------------------------------------------------
# RECOMMENDATION FUNCTION
# --------------------------------------------------

def recommend_movies(movie_title, number_of_recommendations=5):

    matching_movies = movies[
        movies["title"].str.lower() == movie_title.lower()
    ]

    if matching_movies.empty:
        return []

    selected_movie_id = matching_movies.iloc[0]["movieId"]

    if selected_movie_id not in movie_user_matrix.index:
        return []

    selected_ratings = movie_user_matrix.loc[
        selected_movie_id
    ]

    similarity_results = []

    for movie_id in movie_user_matrix.index:

        if movie_id == selected_movie_id:
            continue

        other_ratings = movie_user_matrix.loc[movie_id]

        # Find users who rated both movies
        common_users = (
            selected_ratings.notna()
            & other_ratings.notna()
        )

        common_count = common_users.sum()

        # Require at least 5 common users
        if common_count < 5:
            continue

        selected_values = selected_ratings[
            common_users
        ]

        other_values = other_ratings[
            common_users
        ]

        # Calculate cosine similarity
        score = cosine_similarity(
            [selected_values.values],
            [other_values.values]
        )[0][0]

        similarity_results.append(
            (movie_id, score, common_count)
        )

    # Sort by similarity
    similarity_results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for movie_id, score, common_count in similarity_results[
        :number_of_recommendations
    ]:

        movie = movies[
            movies["movieId"] == movie_id
        ]

        if not movie.empty:

            recommendations.append({
                "title": movie.iloc[0]["title"],
                "genres": movie.iloc[0]["genres"],
                "score": score,
                "common_users": common_count
            })

    return recommendations


# --------------------------------------------------
# USER INTERFACE
# --------------------------------------------------

st.title("🎬 Basic Recommendation System")

st.write(
    "Select a movie and get recommendations "
    "based on user rating patterns."
)

st.divider()


movie_list = sorted(
    movies["title"]
    .dropna()
    .unique()
    .tolist()
)

selected_movie = st.selectbox(
    "Select a movie:",
    movie_list
)


if st.button("🎯 Recommend Movies"):

    recommendations = recommend_movies(
        selected_movie,
        5
    )

    st.subheader(
        f"Recommendations for {selected_movie}"
    )

    if recommendations:

        for number, movie in enumerate(
            recommendations,
            start=1
        ):

            st.write(
                f"### {number}. {movie['title']}"
            )

            st.write(
                f"Genres: {movie['genres']}"
            )

            st.write(
                f"Similarity Score: "
                f"{movie['score']:.2f}"
            )

            st.write(
                f"Common Users: "
                f"{movie['common_users']}"
            )

            st.divider()

    else:

        st.warning(
            "Not enough rating data available "
            "for this movie."
        )


# --------------------------------------------------
# ABOUT PROJECT
# --------------------------------------------------

with st.expander("About this project"):

    st.write(
        """
        Basic Recommendation System

        This project uses collaborative filtering
        to recommend movies.

        Movie ratings from users are organized into
        a movie-user matrix.

        Movies are compared using rating patterns
        from users who rated both movies.

        At least 5 common users are required to
        calculate a recommendation similarity.

        Dataset: MovieLens
        """
    )