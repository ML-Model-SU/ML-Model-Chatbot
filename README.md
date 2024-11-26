# Chatbot with Machine Learning Knowledge Base

## Overview
This chatbot uses text from a machine learning book as its knowledge base. It employs vector embeddings for information retrieval and allows users to query the database.

## Setup
1. Install dependencies:
   ```bash
   pip install -r src/requirements.txt
2. Setup the database
   psql -U <username> -d <dbname> -f setup.sql
3. Run the chatbot
   python src/chatbot.py

---

### Next Steps

1. Replace placeholders like `your_db_name`, `your_username`, and `your_password` with actual credentials.
2. Populate the `machine_learning_book.txt` file with content from your ML book.
3. Run the `chatbot.py` script to test your system.

Let me know if you need further assistance!

