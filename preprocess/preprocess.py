import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# reading dataset
data = pd.read_csv('movie_metadata.csv')

# keep important features which can help to recommend movies, drop others
data = data.drop(
    [
        'color',
        'num_critic_for_reviews',
        'duration',
        'director_facebook_likes',
        'actor_3_facebook_likes',
        'actor_1_facebook_likes',
        'gross',
        'num_voted_users',
        'cast_total_facebook_likes',
        'facenumber_in_poster',
        'plot_keywords',
        'movie_imdb_link',
        'num_user_for_reviews',
        'language',
        'country',
        'content_rating',
        'budget',
        'title_year',
        'actor_2_facebook_likes',
        'imdb_score',
        'aspect_ratio',
        'movie_facebook_likes',
    ],
    axis=1,
)

# Text Preprocessing
data.dropna(inplace=True)

# clean genres--- remove | between generes
data['genres'] = data['genres'].apply(lambda a: str(a).replace('|', ' '))

# clean movie_title column
data['movie_title'] = data['movie_title'].apply(lambda a: a[:-1])

# combined features on which we will calculate cosine similarity
data['combined'] = (
    data['director_name']
    + ' '
    + data['actor_2_name']
    + ' '
    + data['genres']
    + ' '
    + data['actor_1_name']
    + ' '
    + data['actor_3_name']
)

# Saving the preprocessed dataset
data.to_csv('../movies_final.csv')
