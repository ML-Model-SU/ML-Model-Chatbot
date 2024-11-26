from embeddings.embedder import generate_embedding
from embeddings.loader import split_text_into_chunks
from db.db_operations import insert_embedding, retrieve_relevant_chunks

def prepare_data():
    """
    Load the text, split it into chunks, generate embeddings, and store them in the database.
    """
    file_path = "../data/machine_learning_book.txt"
    chunks = split_text_into_chunks(file_path)
    
    for chunk in chunks:
        embedding = generate_embedding(chunk)
        insert_embedding(chunk, embedding)

def chatbot():
    """
    Chatbot interface for querying and generating answers.
    """
    while True:
        query = input("Enter your query: ")
        if query.lower() in ['exit', 'quit']:
            break

        query_embedding = generate_embedding(query)
        relevant_chunks = retrieve_relevant_chunks(query_embedding)
        print("Relevant Information:\n", "\n".join(relevant_chunks))

if __name__ == "__main__":
    prepare_data()
    chatbot()
