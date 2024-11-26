import unittest
from src.db.db_operations import insert_embedding, retrieve_relevant_chunks

class TestDBOperations(unittest.TestCase):
    def test_insert_and_retrieve(self):
        content = "Test content"
        embedding = [0.1] * 384  # Dummy embedding
        insert_embedding(content, embedding)

        query_embedding = [0.1] * 384
        results = retrieve_relevant_chunks(query_embedding)
        self.assertIn(content, results)

if __name__ == "__main__":
    unittest.main()
