from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment variables or .env file.")

def chunk_text(text, max_length=2024):
    """
    Break text into chunks of manageable size.
    :param text: The text to chunk.
    :param max_length: Maximum length of each chunk.
    :return: List of text chunks.
    """
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(" ".join(current_chunk) + " " + word) <= max_length:
            current_chunk.append(word)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

def summarize(row_answer, model="llama3-8b-8192"):  # yha query
    """
    Summarize the relevant answer using Groq's LLM, handling large content by chunking.
    :param query: User query.
    :param row_answer: Relevant chunks from the database.
    :param model: Groq LLM model to use.
    :return: Summarized answer.
    """
    from groq import Groq  # Import inside to avoid issues when API key is missing

    client = Groq(api_key=api_key)

    # Combine all chunks into a single string
    full_context = " ".join(row_answer)
    chunks = chunk_text(full_context)

    summarized_parts = []
    for i, chunk in enumerate(chunks, start=1):   # ISME BHI
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""
                  
                    Context: {chunk}
                    This is part {i} of the context. explaned it related.
                    """
                }
            ],
            model=model,
        )
        summarized_parts.append(chat_completion.choices[0].message.content)

    # Combine summarized parts into a final summary
    final_summary = " ".join(summarized_parts)

    # Optionally, summarize the combined summary if it's still too long
    # if len(final_summary) > 2024:        # ISME BHI
    #     final_summary = client.chat.completions.create(
    #         messages=[
    #             {
    #                 "role": "user",
    #                 "content": f"""
                 
    #                 Context: {final_summary}
    #                 This is the combined summary. Further summarize this to return a concise answer approx 300 words .
    #                 """
    #             }
    #         ],
    #         model=model,
    #     ).choices[0].message.content

    return final_summary
