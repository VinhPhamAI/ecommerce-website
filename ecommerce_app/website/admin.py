from import_export import resources
from .models import Book, Profile, Product
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

class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'first_name', 'last_name', 'email', 'phone_number', 
                  'gender', 'date_of_birth', 'address', 'cart_books')
        export_order = ('id', 'user', 'first_name', 'last_name', 'email', 
                        'phone_number', 'gender', 'date_of_birth', 'address')

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'cart_books_list')
    search_fields = ('first_name', 'last_name', 'email', 'user__username')
    list_filter = ('gender', 'date_of_birth')
    def cart_books_list(self, obj):
        return ", ".join([book.title for book in obj.cart_books.all()])
    cart_books_list.short_description = 'Cart Books'

class ProductForm(resources.ModelResource):
    class Meta:
        model = Product
        fields = ['title', 'isbn', 'price', 'stock', 'author', 'publisher', 'binding', 'pages', 'image_link', 'description']
        exclude = ['user']  # Exclude user from the form since it's set in the view

