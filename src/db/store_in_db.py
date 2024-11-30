import pandas as pd
from src.embeddings.embedder import generate_embedding
from src.db.db_operations import insert_embedding


df = pd.read_csv(r"data\extracted_text5.csv")
row_content = df["Paragraph"]
for row in row_content:
  content = row
  embedding = generate_embedding(row)
  insert_embedding(content, embedding)
