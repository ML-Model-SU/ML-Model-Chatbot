from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if __name__ == "__main__":
    # Example usage
    pdf_path = "../data/machine_learning_book.pdf"
    output_path = "../data/extracted_text.txt"

    text = extract_text_from_pdf(pdf_path)
    with open(output_path, "w") as f:
        f.write(text)
    print(f"Text extracted and saved to {output_path}")
