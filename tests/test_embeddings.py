import unittest
from src.embeddings.embedder import generate_embedding

class TestEmbedding(unittest.TestCase):
    def test_embedding_shape(self):
        text = "Test text"
        embedding = generate_embedding(text)
        self.assertEqual(len(embedding), 384)

if __name__ == "__main__":
    unittest.main()
