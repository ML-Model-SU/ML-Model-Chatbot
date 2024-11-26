 # Database connection configurations

import psycopg2
from psycopg2.extras import execute_val
from pgvector.psycopg2 import register_vector

# Database connection configuration
DB_CONFIG = {
    "host": "localhost",      # Replace with your DB host
    "port": 5432,             # Default PostgreSQL port
    "dbname": "MLdata",       # Your project database name
    "user": "postgres",       # Your PostgreSQL username
    "password": "#RNJ7773RNJ7773"  # Replace with your password
}

# Establish database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        register_vector(conn)  # Register pgvector functionality
        print("Database connection established.")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Create necessary tables
def initialize_db():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()

            # Create pgvector extension
            cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")

            # Create embeddings table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS embeddings (
                id SERIAL PRIMARY KEY,
                document_id TEXT,
                embedding vector(1536), -- Adjust dimension as needed
                metadata JSONB
            );
            """)

            # Create feedback table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id SERIAL PRIMARY KEY,
                query TEXT NOT NULL,
                response TEXT NOT NULL,
                rating INTEGER,
                comments TEXT
            );
            """)

            conn.commit()
            print("Tables created successfully.")
        except psycopg2.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

# Run the initializer
if __name__ == "__main__":
    initialize_db()
