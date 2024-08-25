import os
import django
import csv
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_app.settings')  # Use 'ecommerce_app.settings' since it's your project directory
django.setup()

from website.models import Book  # Adjust this import to your actual model path

def import_books(csv_file_path):
    try:
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Book.objects.update_or_create(
                    isbn=row['isbn'],
                    defaults={
                        'title': row['title'],
                        'author': row['author'],
                        'year_of_publication': row.get('year_of_publication', None),
                        'publisher': row['publisher'],
                        'image_url_l': row.get('image_url_l', None),
                        'price': row.get('price', None),
                        'genres': row.get('genres', ''),
                        'rating': row.get('rating', None),
                        'description': row.get('description', ''),
                        'pages': row.get('pages', ''),
                        'number_of_books': row.get('number_of_books', 0),
                    }
                )
        print('Successfully imported book data from CSV')
    except Exception as e:
        print(f'Error importing data: {e}')

# Call the function with the path to your CSV
import_books('/app/data.csv')  # Adjust the path to where your CSV file is located
