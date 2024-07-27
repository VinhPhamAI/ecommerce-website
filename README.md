# Ecommerce Website



## How to Push Code to a Branch

1. Initialize Git repository (if not already initialized):
    ```sh
    git init
    ```

2. Add all changes to the staging area:
    ```sh
    git add .
    ```

3. Commit the changes:
    ```sh
    git commit -m "your update"
    ```

4. Push the changes to your branch:
    ```sh
    git push origin "your branch"
    ```

5. To generate a personal access token for authentication:
    - Go to `Settings` -> `Developer settings` -> `Personal access tokens` -> `Tokens (classic)`.
  
## Set up a database
[https://www.youtube.com/watch?v=fV2uG92r5EQ&list=PLx-q4INfd95G-wrEjKDAcTB1K-8n1sIiz&index=3](Tutorial)


## Troubleshooting

### Login Issues

If you encounter login issues, follow these steps:

1. Switch to the PostgreSQL user:
    ```sh
    sudo -i -u postgres
    ```

2. Access PostgreSQL:
    ```sh
    psql
    ```

3. Update the PostgreSQL user password:
    ```sql
    ALTER USER postgres WITH PASSWORD 'your_new_password';
    ```

4. Exit PostgreSQL:
    ```sh
    \q
    ```

### Missing Database

If the specified database does not exist:

1. Access PostgreSQL:
    ```sh
    psql
    ```

2. Create the database:
    ```sql
    CREATE DATABASE ecommerce_database;
    ```

3. Exit PostgreSQL:
    ```sh
    \q
    ```

4. Apply migrations:
    ```sh
    python3 manage.py migrate
    ```

5. Run the development server:
    ```sh
    python3 manage.py runserver
    ```

## Running the Development Server

1. Apply database migrations:
    ```sh
    python3 manage.py migrate
    ```

2. Create a superuser (if needed):
    ```sh
    python3 manage.py createsuperuser
    ```

3. Run the development server:
    ```sh
    python3 manage.py runserver
    ```

## Configuration

Ensure your `settings.py` is configured correctly for the database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce_database',
        'USER': 'postgres',
        'PASSWORD': '261223',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
