import pandas as pd
import numpy as np
from pathlib import Path
import re
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

def data_process():
    books_path = Path('website/AI/final.csv')
    ratings_path = Path('website/AI/ratings.csv')
    users_path = Path('website/AI/users.csv')
    books_df = pd.read_csv(books_path,sep=',',on_bad_lines='warn', encoding='latin-1',
        dtype={
            'isbn': str,
            'title': str,
            'author': str,
            'year_of_publication': str,
            'publisher': str,
            'price': str,
            'genres': str,
            'rating': str,
            }
        )
    # Read CSV
    books_df.rename(columns={'isbn': 'ISBN'}, inplace=True)
    ratings_df = pd.read_csv(ratings_path, sep=';', on_bad_lines='warn', encoding='latin-1')
    users_df = pd.read_csv(users_path, sep=';', on_bad_lines='warn', encoding='latin-1')
    users_df.loc[(users_df['Age'] > 90) | (users_df['Age'] < 5), 'Age'] = np.nan
    users_df['Age'] = users_df['Age'].fillna(users_df['Age'].mean())
    users_df['Age'] = users_df['Age'].astype(np.int32)
    users_df = users_df[users_df['Location'] != 'n/a, n/a, n/a']
    ratings_df = ratings_df[ratings_df['Book-Rating'] != 0]

    # MODEL
    user_ratings_df = pd.merge(users_df, ratings_df, on='User-ID')
    books_user_ratings_df = pd.merge(user_ratings_df, books_df, on='ISBN', how='inner')

    book_ids = pd.unique(books_user_ratings_df['ISBN'].to_numpy())
    book_ids = pd.Series(np.arange(len(book_ids)), book_ids)
    book_ids = pd.DataFrame(book_ids)
    book_ids.reset_index(inplace=True)
    book_ids.rename(columns = {'index':'ISBN', 0:'Book-ID'}, inplace=True)
    books_user_ratings_df = pd.merge(books_user_ratings_df, book_ids, on='ISBN', how="inner")
    return books_user_ratings_df


