import pandas as pd
from embeddings.embedder import generate_embedding
from db_operations import insert_embedding
df = pd.read_csv(r"data\extracted_text2.csv")
row_content = df["Paragraph"]
for row in row_content:
  content = row
  embedding = generate_embedding(row)
  insert_embedding(content, embedding)
