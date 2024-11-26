import psycopg2

def get_db_connection():
    """
    Establish a connection to the PostgreSQL database.
    :return: Connection object.
    """
    return psycopg2.connect(
        dbname="your_db_name",
        user="your_username",
        password="your_password",
        host="localhost",
        port=5432
    )
