import os
from groq import Groq

os.environ["GROQ_API_KEY"] = "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"

def summarize(query, row_answer):
  client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
  )

  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": f"""
              query: {query}
              Context: {row_answer}
              this is the relevant answer extracted from my database for given query. Understand this and summarize it. Return the summarize answer."""
          }
      ],
      model="llama3-8b-8192",
  )

  return chat_completion.choices[0].message.content