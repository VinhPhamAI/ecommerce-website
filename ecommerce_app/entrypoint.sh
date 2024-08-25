#!/bin/bash

# Function to wait for PostgreSQL
wait_for_postgres() {
  echo "Waiting for PostgreSQL to start..."
  while ! python -c "import psycopg2; psycopg2.connect(dbname='${POSTGRES_DB}', user='${POSTGRES_USER}', password='${POSTGRES_PASSWORD}', host='db')"; do
    sleep 0.1
  done
  echo "PostgreSQL started"
}

# Wait for PostgreSQL to start
wait_for_postgres

# Run migrations
echo "Running Django migrations..."
python manage.py migrate

# Create superuser if not exists
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    echo "Creating superuser..."
    echo "from django.contrib.auth.models import User; User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists() or User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell
else
    echo "Superuser credentials are not fully set in the environment variables. Skipping superuser creation."
fi

# Set PYTHONPATH to include the project directory
export PYTHONPATH=$PYTHONPATH:/app

# Import data from CSV directly using the Python script
echo "Importing data from CSV..."
python /app/management/commands/import_books.py  # Ensure this path is correct

# Run the Django server
exec python manage.py runserver 0.0.0.0:8000
