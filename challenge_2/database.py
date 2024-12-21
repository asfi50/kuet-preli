import sqlite3

DB_NAME = "ingredients.db"

def get_connection():
    """Returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # Return results as dictionaries
    return conn




def init_db():
    """Initializes the database and creates the ingredients table."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            quantity TEXT,
            unit TEXT,
            calories INTEGER DEFAULT 0,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()
