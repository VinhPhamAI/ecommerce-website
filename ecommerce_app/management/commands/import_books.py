import csv
from django.core.management.base import BaseCommand
from your_app.models import Book  # Replace 'your_app' with the name of your Django app

class Command(BaseCommand):
    help = 'Import book data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import data from')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

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
            self.stdout.write(self.style.SUCCESS('Successfully imported book data from CSV'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing data: {e}'))
