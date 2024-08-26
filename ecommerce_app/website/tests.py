from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Book, ShoppingCart, Product, Order, OrderItems

class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile = Profile.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com'
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.first_name, 'John')
        self.assertEqual(self.profile.last_name, 'Doe')
        self.assertEqual(self.profile.email, 'johndoe@example.com')

class BookModelTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            isbn='1234567890123',
            title='Test Book',
            author='Author Name',
            year_of_publication=2021,
            publisher='Test Publisher',
            price=19.99
        )

    def test_book_creation(self):
        self.assertEqual(self.book.isbn, '1234567890123')
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, 'Author Name')
        self.assertEqual(self.book.year_of_publication, 2021)
        self.assertEqual(self.book.publisher, 'Test Publisher')
        self.assertEqual(self.book.price, 19.99)

class ShoppingCartModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile = Profile.objects.create(user=self.user)
        self.book = Book.objects.create(
            isbn='1234567890123',
            title='Test Book',
            author='Author Name',
            year_of_publication=2021,
            publisher='Test Publisher',
            price=19.99
        )
        self.cart_item = ShoppingCart.objects.create(
            profile=self.profile,
            book=self.book,
            quantity=2
        )

    def test_shopping_cart_creation(self):
        self.assertEqual(self.cart_item.profile.user.username, 'testuser')
        self.assertEqual(self.cart_item.book.title, 'Test Book')
        self.assertEqual(self.cart_item.quantity, 2)

class ProductModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.product = Product.objects.create(
            user=self.user,
            title='Test Product',
            price=49.99
        )

    def test_product_creation(self):
        self.assertEqual(self.product.user.username, 'testuser')
        self.assertEqual(self.product.title, 'Test Product')
        self.assertEqual(self.product.price, 49.99)

class OrderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.book = Book.objects.create(
            isbn='1234567890123',
            title='Test Book',
            author='Author Name',
            year_of_publication=2021,
            publisher='Test Publisher',
            price=19.99
        )
        self.order = Order.objects.create(
            user=self.user,
            name='John Doe',
            email='johndoe@example.com',
            price=19.99,
            shipping_cost=5.00,
            total_cost=24.99
        )
        self.order_item = OrderItems.objects.create(
            order=self.order,
            book=self.book,
            quantity=1,
            price=19.99
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user.username, 'testuser')
        self.assertEqual(self.order.name, 'John Doe')
        self.assertEqual(self.order.email, 'johndoe@example.com')
        self.assertEqual(self.order.price, 19.99)
        self.assertEqual(self.order.shipping_cost, 5.00)
        self.assertEqual(self.order.total_cost, 24.99)

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.book.title, 'Test Book')
        self.assertEqual(self.order_item.quantity, 1)
        self.assertEqual(self.order_item.price, 19.99)
