import sqlite3
import os

from flask import current_app, g


# Paths to the SQLite database files
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'healthtracker.db')
SCHEMA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'schema.sql')

def get_db():
    db = getattr(g, '_database', None)
    if db is None: 
        db = g._database = sqlite3.connect(DATABASE)
    return db

get_db()