import os

import psycopg
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Module 4 - Docker & Containerization</h1>
    <h2>Zero Trust Pro</h2>
    <p>Flask application is running successfully inside Docker.</p>
    <p>Use /db-test to test PostgreSQL connectivity.</p>
    <p>Submitted by Sikandar Shah</p>
    """


@app.route("/db-test")
def db_test():
    try:
        connection = psycopg.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("POSTGRES_DB", "module4db"),
            user=os.getenv("POSTGRES_USER", "module4user"),
            password=os.getenv("POSTGRES_PASSWORD", "change-this-password"),
        )

        connection.close()

        return "<h2>Database connection successful!</h2>"

    except Exception as error:
        return f"<h2>Database connection failed:</h2><p>{error}</p>", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)