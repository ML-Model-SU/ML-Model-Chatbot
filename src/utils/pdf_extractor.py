# from PyPDF2 import PdfReader

# def extract_text_from_pdf(pdf_path):
#     """
#     Extracts text from a PDF file.
#     :param pdf_path: Path to the PDF file.
#     :return: Extracted text as a string.
#     """
#     reader = PdfReader(pdf_path)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text

# if __name__ == "__main__":
#     # Example usage
#     pdf_path = "../data/machine_learning_book.pdf"
#     output_path = "../data/extracted_text.txt"

#     text = extract_text_from_pdf(pdf_path)
#     with open(output_path, "w") as f:
#         f.write(text)
#     print(f"Text extracted and saved to {output_path}")

from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from the given PDF file.
    """
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        if page.extract_text():
            full_text += page.extract_text() + "\n"  # Add page content and newline
    return full_text

def save_text_to_file(text, output_file):
    """
    Saves the extracted text to a .txt file.
    """
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

# File paths
pdf_path = r"data\Machine_Learning.pdf"  # Replace with your PDF file path
output_file = r"data\extracted_texts.txt"

# Process PDF and save text
text = extract_text_from_pdf(pdf_path)
save_text_to_file(text, output_file)

print(f"Extracted text saved to {output_file}")
