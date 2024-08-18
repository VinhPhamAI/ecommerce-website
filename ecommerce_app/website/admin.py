from import_export import resources
from .models import Book
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        fields = ('isbn', 'title', 'author', 'year_of_publication', 'publisher', 'image_url_l', 'price', 'genres', 'rating', 'description', 'pages', 'number_of_books')
        import_id_fields = ['isbn']

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    list_display = ('title', 'author', 'publisher', 'price', 'rating', 'genres', 'description', 'pages')  # Include new fields in list_display
    search_fields = ('title', 'author', 'isbn', 'genres')  # Include new fields in search_fields
