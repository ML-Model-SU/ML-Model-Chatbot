import psycopg2

def get_db_connection():
    """
    Establish a connection to the PostgreSQL database.
    :return: Connection object.
    """
    return psycopg2.connect(
        dbname="mldata",
        user="postgres",
        password="#RNJ7773RNJ7773",
        host="localhost",
        port=5433
    )
