import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'mindflow.db'))
SCHEMA_PATH = os.path.abspath(os.path.join(BASE_DIR, 'schema.sql'))

def init_db():
    """Initialize the SQLite database using the schema definitions."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Ensure foreign key support
    cursor.execute('PRAGMA foreign_keys = ON;')
    # Execute all CREATE TABLE statements from schema.sql
    with open(SCHEMA_PATH, 'r') as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()