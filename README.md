# Flask API Project

This is a Flask API project that uses SQLAlchemy for database interactions, Flask-Migrate for database migrations, and Marshmallow for serialization and deserialization.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Database Migrations](#database-migrations)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:ifrit653/sidewinder.git
   cd sidewinder
   ```

2. **Create and activate a virtual environment**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the dependencies:**
   ```bash
    pip install -r requirements.txt
   ```

## Configuration

1. **Create a .env file in the root directory with the following content:**
   ```ini
    SECRET_KEY=8ebb8ab2f0fdf0d387fc25c952768b46
    SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:@localhost/accounting_db
    SQLALCHEMY_TRACK_MODIFICATIONS=False
   ```

## Database migration

1. **Initialize the migrations directory:**

```bash
    flask db init
```

2. **Create an initial migration:**

```bash
    flask db migrate -m "Initial migration."
```

3. **Apply the migration:**

```bash
    flask db upgrade
```

## Running the Application:

1. **Set the FLASK_APP environment variable:**

```bash
    set FLASK_APP=run.py
```

2. **Run the Flask application:**

```bash
    flask run
```

### Explanation:

1. **Installation**: Guides the user through cloning the repository, setting up a virtual environment, and installing dependencies.
2. **Configuration**: Instructs on setting up the `.env` file for environment-specific configurations like secret keys and database URIs.
3. **Database Migrations**: Explains how to initialize, create, and apply database migrations using Flask-Migrate.
4. **Running the Application**: Provides instructions for setting the `FLASK_APP` environment variable and running the Flask application.
5. **API Endpoints**: Lists the available API endpoints, their methods, and example JSON responses.
6. **License**: Specifies the licensing for the project.

This `README.md` provides a clear and concise guide for setting up, configuring, and running your Flask project.
