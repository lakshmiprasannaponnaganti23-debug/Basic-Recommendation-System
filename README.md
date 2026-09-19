# Basic Recommendation System

## Author

**Lakshmi Prasanna Ponnaganti**

## Domain

**Artificial Intelligence and Machine Learning (AI/ML)**

### Sub-domain

**Recommendation Systems / Recommender Systems**

---

## Project Overview

The **Basic Recommendation System** is a machine learning project that recommends movies to users based on rating patterns.

The project uses the **MovieLens dataset** and implements **item-based collaborative filtering**.

Users can select a movie through a Streamlit web application, and the system recommends five movies that have similar rating patterns.

---

## Objective

The main objective of this project is to understand and implement the basic concepts of recommendation systems using machine learning.

The system analyzes interactions between users and movies using their ratings and generates movie recommendations based on similar rating patterns.

---

## Technologies Used

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **Web Framework:** Streamlit
* **Dataset:** MovieLens

---

## Dataset

This project uses the **MovieLens dataset**.

The dataset contains information about movies and user ratings.

### Main files used

* `movies.csv` — contains movie IDs, movie titles, and genres.
* `ratings.csv` — contains user IDs, movie IDs, ratings, and timestamps.

---

## Recommendation Approach

This project uses **Item-Based Collaborative Filtering**.

The system recommends movies by comparing the rating patterns of different movies.

### Process

1. Load the MovieLens dataset.
2. Prepare the movie and rating data.
3. Create a movie-user rating matrix.
4. Identify users who rated both movies.
5. Calculate similarity between movies.
6. Use cosine similarity to compare rating patterns.
7. Rank similar movies.
8. Display the top five movie recommendations.

---

## System Workflow

```text
MovieLens Dataset
       |
       v
Data Collection and Preparation
       |
       v
Data Preprocessing
       |
       v
Movie-User Rating Matrix
       |
       v
Item-Based Collaborative Filtering
       |
       v
Common User Ratings
       |
       v
Cosine Similarity
       |
       v
Movie Similarity Ranking
       |
       v
Top 5 Movie Recommendations
       |
       v
Streamlit Web Application
```

---

## Project Structure

```text
Basic Recommendation System
│
├── data
│   ├── movies.csv
│   └── ratings.csv
│
├── src
│   ├── explore_data.py
│   ├── recommendation.py
│   ├── rating_recommendation.py
│   └── collaborative_filtering.py
│
├── app.py
├── README.md
└── venv
```

---

## Data Preprocessing

The rating data is transformed into a **movie-user matrix**.

In this matrix:

* Rows represent movies.
* Columns represent users.
* Values represent user ratings.
* Missing values indicate that a user has not rated a particular movie.

The system then identifies users who have rated both the selected movie and another movie.

A minimum number of common users is used before calculating similarity.

---

## Collaborative Filtering

### What is Collaborative Filtering?

Collaborative filtering is a recommendation technique that uses the behavior or preferences of users to recommend items.

In this project:

* **Users** are MovieLens users.
* **Items** are movies.
* **User behavior** is represented by movie ratings.

If two movies receive similar ratings from users, they can be considered similar and one can be recommended when the other is selected.

---

## Cosine Similarity

The project uses **cosine similarity** to compare the rating patterns between movies.

A higher similarity score indicates that the rating patterns of two movies are more similar.

For example:

```text
Selected Movie
      |
      v
Compare rating pattern
      |
      v
Other movies
      |
      v
Calculate similarity
      |
      v
Rank movies
      |
      v
Top 5 recommendations
```

---

## Streamlit Application

The project includes an interactive Streamlit web application.

### Application Features

* Movie selection dropdown
* Recommendation button
* Top five movie recommendations
* Movie genres
* Similarity score
* Number of common users
* Project information section

---

## How to Run the Project

### Step 1: Open the project folder

```powershell
cd "C:\Users\Naras\Downloads\Basic Recommendation System"
```

### Step 2: Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install required libraries

```powershell
python -m pip install pandas numpy scikit-learn streamlit
```

### Step 4: Run the Streamlit application

```powershell
streamlit run app.py
```

The application will open in the browser.

---

## How to Use the Application

1. Open the Streamlit application.
2. Select a movie from the dropdown.
3. Click **Recommend Movies**.
4. The system analyzes movie rating patterns.
5. The system generates five recommendations.
6. Each recommendation displays:

   * Movie title
   * Genre
   * Similarity score
   * Number of common users

---

## Learning Outcomes

Through this project, the following concepts were learned:

* Recommendation system fundamentals
* Collaborative filtering
* User-item interaction data
* Data preprocessing
* Rating matrices
* Cosine similarity
* Recommendation generation
* Pandas data manipulation
* Scikit-learn machine learning techniques
* Streamlit application development

---

## Project Requirements Covered

The project satisfies the core requirements of the Basic Recommendation System.

| Requirement                 | Implementation                     |
| --------------------------- | ---------------------------------- |
| Data Collection/Preparation | MovieLens dataset                  |
| Data Preprocessing          | Movie-user rating matrix           |
| Recommendation Algorithm    | Item-based collaborative filtering |
| Recommendation Generation   | Top five similar movies            |
| Programming Language        | Python                             |
| Libraries                   | Pandas, NumPy, Scikit-learn        |
| Dataset                     | MovieLens                          |
| Interactive Application     | Streamlit                          |

### Evaluation

Evaluation using metrics such as **precision and recall** is listed as optional in the project requirements. The current implementation focuses on the required recommendation-system functionality.

---

## Advantages

* Uses a real-world movie rating dataset.
* Demonstrates a practical machine learning application.
* Uses collaborative filtering.
* Provides interactive recommendations.
* Easy to extend to other recommendation domains.
* Demonstrates important data preprocessing and similarity concepts.

---

## Applications

The same recommendation approach can be adapted for:

* Movie recommendation systems
* Product recommendation systems
* Music recommendation systems
* Book recommendation systems
* Course recommendation systems
* News recommendation systems

---

## Future Enhancements

The system can be improved in the future by adding:

* Precision and recall evaluation
* User-based collaborative filtering
* Hybrid recommendation using ratings and genres
* Personalized recommendations for individual users
* Movie search functionality
* Movie posters and additional movie information
* User login and rating functionality
* Online deployment

---

## Conclusion

The **Basic Recommendation System** successfully demonstrates how machine learning and collaborative filtering can be used to generate movie recommendations.

The system performs data preparation, preprocessing, creates a movie-user rating matrix, compares movies using rating patterns and cosine similarity, and generates recommendations through an interactive Streamlit application.

The project provides practical experience with recommendation-system concepts, data preprocessing, collaborative filtering, similarity calculation, and machine learning application development.

---

## Author

**Lakshmi Prasanna Ponnaganti**

B.Tech Computer Science and Engineering
