from embeddings.embedder import generate_embedding
from db.db_operations import retrieve_relevant_chunks
from llma_connection import summarize
def answer():
    """
    Chatbot interface for querying and generating answers.
    """
    while True:
        query = input("Enter your query: ")
        if query.lower() in ['exit', 'quit']:
            break

        query_embedding = generate_embedding(query)
        relevant_chunks = retrieve_relevant_chunks(query_embedding)
        summarize_answer = summarize(query, relevant_chunks)
        return summarize_answer

