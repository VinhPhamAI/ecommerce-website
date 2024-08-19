from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
import numpy as np
from data import books_user_ratings_df

def create_matrix(df):

    N = len(df['User-ID'].unique())
    M = len(df['Book-ID'].unique())

    # Map IDs to indices
    user_mapper = dict(zip(np.unique(df["User-ID"]), list(range(N))))
    book_mapper = dict(zip(np.unique(df["Book-ID"]), list(range(M))))

    # Map indices to IDs
    user_inv_mapper = dict(zip(list(range(N)), np.unique(df["User-ID"])))
    book_inv_mapper = dict(zip(list(range(M)), np.unique(df["Book-ID"])))

    user_index = [user_mapper[i] for i in df['User-ID']]
    book_index = [book_mapper[i] for i in df['Book-ID']]

    X = csr_matrix((df["Book-ID"], (book_index, user_index)), shape=(M, N))

    return X, user_mapper, book_mapper, user_inv_mapper, book_inv_mapper

X, user_mapper, book_mapper, user_inv_mapper, book_inv_mapper = create_matrix(books_user_ratings_df)

def find_similar_books(book_id, X, k, metric='cosine', show_distance=False):

    neighbour_ids = []
    
    book_ind = book_mapper[book_id]
    book_vec = X[book_ind]
    k+=1
    kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
    kNN.fit(X)
    book_vec = book_vec.reshape(1,-1)
    neighbour = kNN.kneighbors(book_vec, return_distance=show_distance)
    for i in range(0,k):
        n = neighbour.item(i)
        neighbour_ids.append(book_inv_mapper[n])
    neighbour_ids.pop(0)
    return neighbour_ids