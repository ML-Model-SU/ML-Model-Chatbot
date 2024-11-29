from embeddings.embedder import generate_embedding
from db.db_operations import retrieve_relevant_chunks
def row_answer():
    """
    Chatbot interface for querying and generating answers.
    """
    while True:
        query = input("Enter your query: ")
        if query.lower() in ['exit', 'quit']:
            break

        query_embedding = generate_embedding(query)
        relevant_chunks = retrieve_relevant_chunks(query_embedding)
        return relevant_chunks

