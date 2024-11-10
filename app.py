from flask import Flask
import click
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from random import random
import datetime

def create_app():
    app = Flask(__name__)

    @app.cli.command('insert-data')
    def insert_data():
        """Insert 100 rows of data into the database."""
        DATABASE_URL = 'postgresql+psycopg2://postgres:new_password@localhost/machine_data'
        engine = create_engine(DATABASE_URL)

        query = text('INSERT INTO public.machine_inputs (timestamp, sensor_type, values) VALUES (:timestamp, :sensor_type, :values)')

        data = [
            {'timestamp': datetime.datetime.now(), 'sensor_type': 'temperature', 'values': random() * 100}
            for _ in range(100)
        ]

        with engine.connect() as connection:
            # Insert each row individually
            for entry in data:
                connection.execute(query, **entry)
        click.echo('100 rows of data inserted successfully.')

    @app.route('/')
    def index():
        return 'Hello, World!'

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development
