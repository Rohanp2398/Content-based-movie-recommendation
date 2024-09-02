# Content-based-movie-recommendation
Movie recommendation based on tags from content, genre, actors.. etc. using BoW

## Overview

This project is a content-based movie recommender system that suggests movies to users based on the content of the movies they like. The system uses the Bag of Words (BoW) model to convert movie descriptions and other textual data into a vectorized form, which is then used to compute similarity scores between movies.

## Features

- **Content-Based Filtering**: Recommends movies similar to a given movie based on plot summaries, genres, cast, and other metadata.
- **Bag of Words Model**: Textual data (like plot summaries and cast information) is converted into numerical features using the Bag of Words technique.
- **Similarity Computation**: The system computes the similarity between movies using cosine similarity based on their BoW vectors.
- **Scalable**: Works with a large dataset of movies, efficiently handling thousands of entries.

## Dataset

The system uses a dataset of movies with the following features:

- **Title**: The title of the movie.
- **Genres**: A list of genres associated with the movie.
- **Plot Summary**: A brief description of the movie's plot.
- **Cast**: A list of main actors in the movie.
- **Keywords**: Important terms associated with the movie.
- **Director**: The director of the movie.

### Example Dataset
| Title        | Genres            | Plot Summary                                   | Cast                               | Keywords        | Director        |
|--------------|-------------------|-----------------------------------------------|------------------------------------|-----------------|-----------------|
| Avatar       | Action, Adventure | A paraplegic Marine is dispatched to Pandora. | Sam Worthington, Zoe Saldana       | alien, future   | James Cameron   |
| Inception    | Action, Sci-Fi    | A thief steals corporate secrets through dream | Leonardo DiCaprio, Joseph Gordon-Levitt | dream, mind-bending | Christopher Nolan |

