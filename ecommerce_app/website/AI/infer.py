from data import books_user_ratings_df
from model import find_similar_books, X

book_titles = dict(zip(books_user_ratings_df['Book-ID'], books_user_ratings_df['title']))
ISBN_id = 109

# Find similar books
similar_ids = find_similar_books(ISBN_id, X, k=10)
book_title = book_titles[ISBN_id]

print(f"Since you read {book_title}:")
for i in similar_ids:
    print(book_titles[i])