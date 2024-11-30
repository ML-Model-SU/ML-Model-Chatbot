from flask import Blueprint, request, jsonify, render_template
from src.embeddings.embedder import generate_embedding
from src.db.db_operations import retrieve_relevant_chunks
from llma_connection import summarize

import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Create a Flask blueprint
routes = Blueprint("routes", __name__)

@routes.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        # Get the query from the submitted form
        query = request.form.get("query", "").strip()
        if not query:
            return render_template("index.html", summarize_answer="Query cannot be empty.")

        # Generate query embedding
        query_embedding = generate_embedding(query)

        # Retrieve relevant chunks from the database
        relevant_chunks = retrieve_relevant_chunks(query_embedding)
        if not relevant_chunks:
            return render_template("index.html", summarize_answer="No relevant data found in the database.")

        # Summarize the retrieved chunks
        summarized_answer = summarize( relevant_chunks)  #//add query if want to give groq.

        # Render the template with the summarized answer
        return render_template("index.html", query = query, summarize_answer=summarized_answer)

    except Exception as e:
        # Handle errors and display them on the page
        return render_template("index.html", summarize_answer=f"Error: {str(e)}")
