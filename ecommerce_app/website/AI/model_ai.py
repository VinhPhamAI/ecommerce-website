from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
import numpy as np
from .data import data_process

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


def find_similar_books(book_id,books_user_ratings_df, k, metric='cosine', show_distance=False):
    neighbour_ids = []
    X, user_mapper, book_mapper, user_inv_mapper, book_inv_mapper = create_matrix(books_user_ratings_df)
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

def infer(Book_isbn):
    # Truy xuất dữ liệu sách và tạo dictionary
    books_user_ratings_df = data_process()
    # Create a mapping from ISBN to Book-ID
    isbn_to_book_id = dict(zip(books_user_ratings_df['ISBN'], books_user_ratings_df['Book-ID']))
    
    # Create a reverse mapping from Book-ID to ISBN
    book_id_to_isbn = {book_id: isbn for isbn, book_id in isbn_to_book_id.items()}

    # Get the Book-ID from the given ISBN
    if Book_isbn not in isbn_to_book_id:
        raise ValueError(f"ISBN {Book_isbn} not found in book_titles")
    
    Book_id = isbn_to_book_id[Book_isbn]

    # Find similar Book-IDs
    similar_ids = find_similar_books(Book_id, books_user_ratings_df, k=12)
    similar_isbns = []

    # Map Book-IDs from similar_ids to ISBNs
    for similar_id in similar_ids:
        if similar_id in book_id_to_isbn:
            similar_isbns.append(book_id_to_isbn[similar_id])

    return similar_isbns

