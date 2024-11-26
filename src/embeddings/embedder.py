from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def generate_embedding(text):
    """
    Generate embedding for a given text.
    :param text: Input string.
    :return: Embedding vector (list of floats).
    """
    return model.encode(text).tolist()
