from db_config import get_db_connection

def insert_embedding(content, embedding):
    """
    Insert content and its embedding into the database.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO embeddings (content, embedding)
        VALUES (%s, %s)
        """,
        (content, embedding)
    )
    conn.commit()
    cur.close()
    conn.close()

def retrieve_relevant_chunks(query_embedding, top_k=3):
    """
    Retrieve the most relevant chunks based on a query embedding.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT content
        FROM embeddings
        ORDER BY embedding <-> %s
        LIMIT %s
        """,
        (query_embedding, top_k)
    )
    results = cur.fetchall()
    cur.close()
    conn.close()
    return [result[0] for result in results]
