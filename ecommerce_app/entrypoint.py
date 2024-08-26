import os
import time
import psycopg2
import django

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_app.settings')  # Replace 'your_project_name' with the actual project name

# Initialize Django
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model

def wait_for_postgres():
    """Wait for PostgreSQL to start."""
    print("Waiting for PostgreSQL to start...")
    while True:
        try:
            conn = psycopg2.connect(
                dbname=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD'),
                host='db'
            )
            conn.close()
            break
        except psycopg2.OperationalError:
            print("PostgreSQL is unavailable - sleeping")
            time.sleep(0.1)
    print("PostgreSQL started")

# Wait for PostgreSQL to start
wait_for_postgres()

# Run Django migrations
print("Running Django migrations...")
try:
    call_command('migrate')
except Exception as e:
    print(f"Migrations failed: {e}")
    exit(1)

# Create superuser if not exists
superuser_username = os.getenv('DJANGO_SUPERUSER_USERNAME')
superuser_password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
superuser_email = os.getenv('DJANGO_SUPERUSER_EMAIL')

if superuser_username and superuser_password and superuser_email:
    User = get_user_model()
    if not User.objects.filter(username=superuser_username).exists():
        print("Creating superuser...")
        try:
            User.objects.create_superuser(superuser_username, superuser_email, superuser_password)
            print("Superuser created successfully.")
        except Exception as e:
            print(f"Superuser creation failed: {e}")
            exit(1)
else:
    print("Superuser credentials are not fully set in the environment variables. Skipping superuser creation.")

# Import data from CSV directly using the Python script
print("Importing data from CSV...")
# Directly run the import_books management command
import management.commands.import_books as import_books_module
import_books_module.import_books('/app/data.csv')


# Run the Django server
print("Starting Django server...")
os.system('python manage.py runserver 0.0.0.0:8000')
