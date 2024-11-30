# # # # from PyPDF2 import PdfReader

# # # # def extract_text_from_pdf(pdf_path):
# # # #     """
# # # #     Extracts text from a PDF file.
# # # #     :param pdf_path: Path to the PDF file.
# # # #     :return: Extracted text as a string.
# # # #     """
# # # #     reader = PdfReader(pdf_path)
# # # #     text = ""
# # # #     for page in reader.pages:
# # # #         text += page.extract_text()
# # # #     return text

# # # # if __name__ == "__main__":
# # # #     # Example usage
# # # #     pdf_path = "../data/machine_learning_book.pdf"
# # # #     output_path = "../data/extracted_text.txt"

# # # #     text = extract_text_from_pdf(pdf_path)
# # # #     with open(output_path, "w") as f:
# # # #         f.write(text)
# # # #     print(f"Text extracted and saved to {output_path}")

# # # from PyPDF2 import PdfReader

# # # # def extract_text_from_pdf(pdf_path):
# # # #     """
# # # #     Extracts text from the given PDF file.
# # # #     """
# # # #     reader = PdfReader(pdf_path)
# # # #     full_text = ""
# # # #     for page in reader.pages:
# # # #         if page.extract_text():
# # # #             full_text += page.extract_text() + "\n"  # Add page content and newline
# # # #     return full_text

# # # # def save_text_to_file(text, output_file):
# # # #     """
# # # #     Saves the extracted text to a .txt file.
# # # #     """
# # # #     with open(output_file, "w", encoding="utf-8") as file:
# # # #         file.write(text)

# # # # # File paths
# # # # pdf_path = r"data\Machine_Learning.pdf"  # Replace with your PDF file path
# # # # output_file = r"data\extracted_texts.txt"

# # # # # Process PDF and save text
# # # # text = extract_text_from_pdf(pdf_path)
# # # # save_text_to_file(text, output_file)

# # # # print(f"Extracted text saved to {output_file}")


# # # from PyPDF2 import PdfReader
# # # import pandas as pd

# # # def extract_text_from_pdf(pdf_path):
# # #     """
# # #     Extracts text from the given PDF file.
# # #     """
# # #     reader = PdfReader(pdf_path)
# # #     full_text = []
# # #     for page in reader.pages:  # Corrected to access pages
# # #         if page.extract_text():
# # #             full_text.append(page.extract_text())  # Append page content
# # #     return "\n".join(full_text)  # Join all pages' text with newline

# # # def save_text_to_file(text, output_file):
# # #     """
# # #     Saves the extracted text to a .txt file.
# # #     """
# # #     with open(output_file, "w", encoding="utf-8") as file:
# # #         file.write(text)

# # # def create_dataframe_from_text(text):
# # #     """
# # #     Creates a DataFrame from the extracted text, splitting it into paragraphs.
# # #     """
# # #     paragraphs = text.strip().split("\n\n")  # Split into paragraphs
# # #     df = pd.DataFrame(paragraphs, columns=["Paragraph"])  # Create DataFrame
# # #     return df

# # # def save_dataframe_to_csv(df, csv_file):
# # #     """
# # #     Saves the DataFrame to a CSV file.
# # #     """
# # #     df.to_csv(csv_file, index=False, encoding="utf-8")  # Save to CSV

# # # # File paths
# # # pdf_path = r"data\Machine_Learning.pdf"  # Replace with your PDF file path
# # # output_txt_file = r"data\extracted_text2.txt"
# # # output_csv_file = r"data\extracted_text2.csv"

# # # # Process PDF and save text
# # # text = extract_text_from_pdf(pdf_path)
# # # save_text_to_file(text, output_txt_file)

# # # # Create DataFrame and save to CSV
# # # df = create_dataframe_from_text(text)
# # # save_dataframe_to_csv(df, output_csv_file)

# # # print(f"Extracted text saved to {output_txt_file} and DataFrame saved to {output_csv_file}")

# # from PyPDF2 import PdfReader
# # import pandas as pd



# # def extract_text_from_pdf(pdf_path):
# #     """
# #     Extracts text from the given PDF file, preserving paragraph breaks.
# #     """
# #     reader = PdfReader(pdf_path)
# #     full_text = []
# #     for page in reader.pages:
# #         if page.extract_text():
# #             page_text = page.extract_text()
# #             # Normalize line breaks and retain paragraph structure
# #             paragraphs = page_text.replace("\r", "").split("\n\n")  # Split into paragraphs
# #             formatted_paragraphs = [paragraph.replace("\n", " ").strip() for paragraph in paragraphs if paragraph.strip()]
# #             full_text.extend(formatted_paragraphs)
# #     return "\n\n".join(full_text)  # Join paragraphs with double newlines

# # def save_text_to_file(text, output_file):
# #     """
# #     Saves the extracted text to a .txt file.
# #     """
# #     with open(output_file, "w", encoding="utf-8") as file:
# #         file.write(text)

# # def create_dataframe_from_text(text):
# #     """
# #     Creates a DataFrame from the extracted text, splitting it into paragraphs.
# #     """
# #     paragraphs = text.strip().split("\n\n")  # Split by double newlines
# #     df = pd.DataFrame(paragraphs, columns=["Paragraph"])  # Create DataFrame with paragraphs
# #     return df

# # def save_dataframe_to_csv(df, csv_file):
# #     """
# #     Saves the DataFrame to a CSV file.
# #     """
# #     df.to_csv(csv_file, index=False, encoding="utf-8")  # Save to CSV

# # # File paths
# # pdf_path = r"data\Machine_Learning.pdf"  # Replace with your PDF file path
# # output_txt_file = r"data\extracted_text2.txt"
# # output_csv_file = r"data\extracted_text2.csv"

# # # Process PDF and save text
# # text = extract_text_from_pdf(pdf_path)
# # save_text_to_file(text, output_txt_file)

# # # Create DataFrame and save to CSV
# # df = create_dataframe_from_text(text)
# # save_dataframe_to_csv(df, output_csv_file)

# # print(f"Extracted text saved to {output_txt_file} and DataFrame saved to {output_csv_file}")

# from PyPDF2 import PdfReader
# import pandas as pd

# class PDFTextExtractor:
#     def __init__(self, pdf_path):
#         """
#         Initialize the PDFTextExtractor with the path to the PDF file.
#         """
#         self.pdf_path = pdf_path
#         self.text = None

#     def extract_text(self):
#         """
#         Extracts text from the given PDF file, preserving paragraph breaks.
#         """
#         reader = PdfReader(self.pdf_path)
#         full_text = []
#         for page in reader.pages:
#             if page.extract_text():
#                 page_text = page.extract_text()
#                 # Normalize line breaks and retain paragraph structure
#                 paragraphs = page_text.replace("\r", "").split("\n\n")
#                 formatted_paragraphs = [
#                     paragraph.replace("\n", " ").strip()
#                     for paragraph in paragraphs if paragraph.strip()
#                 ]
#                 full_text.extend(formatted_paragraphs)
#         self.text = "\n\n".join(full_text)  # Join paragraphs with double newlines
#         return self.text

#     def save_text_to_file(self, output_file):
#         """
#         Saves the extracted text to a .txt file.
#         """
#         if self.text is None:
#             raise ValueError("No text extracted. Call `extract_text` first.")
#         with open(output_file, "w", encoding="utf-8") as file:
#             file.write(self.text)

#     def create_dataframe(self):
#         """
#         Creates a DataFrame from the extracted text, splitting it into paragraphs.
#         """
#         if self.text is None:
#             raise ValueError("No text extracted. Call `extract_text` first.")
#         paragraphs = self.text.strip().split("\n\n")  # Split by double newlines
#         df = pd.DataFrame(paragraphs, columns=["Paragraph"])
#         return df

#     def save_dataframe_to_csv(self, df, csv_file):
#         """
#         Saves the DataFrame to a CSV file.
#         """
#         df.to_csv(csv_file, index=False, encoding="utf-8")  # Save to CSV

# # Usage example
# if __name__ == "__main__":
#     # File paths
#     pdf_path = r"data\MLBOOK.pdf"  # Replace with your PDF file path
#     output_txt_file = r"data\extracted_text5.txt"
#     output_csv_file = r"data\extracted_text5.csv"

#     # Create an instance of PDFTextExtractor
#     extractor = PDFTextExtractor(pdf_path)

#     # Extract text
#     text = extractor.extract_text()

#     # Save text to file
#     extractor.save_text_to_file(output_txt_file)

#     # Create DataFrame
#     df = extractor.create_dataframe()

#     # Save DataFrame to CSV
#     extractor.save_dataframe_to_csv(df, output_csv_file)

#     print(f"Extracted text saved to {output_txt_file} and DataFrame saved to {output_csv_file}")


import re
from PyPDF2 import PdfReader
import pandas as pd

class PDFTextExtractor:
    def __init__(self, pdf_path):
        """
        Initialize the PDFTextExtractor with the path to the PDF file.
        """
        self.pdf_path = pdf_path
        self.text = None

    def extract_text(self):
        """
        Extracts text from the given PDF file, preserving paragraph breaks
        and reducing multiple full stops to a single full stop.
        """
        reader = PdfReader(self.pdf_path)
        full_text = []
        for page in reader.pages:
            if page.extract_text():
                page_text = page.extract_text()
                # Normalize line breaks and retain paragraph structure
                paragraphs = page_text.replace("\r", "").split("\n\n")
                formatted_paragraphs = [
                    re.sub(r"\.{2,}", ".", paragraph.replace("\n", " ").strip())  # Replace multiple full stops with one
                    for paragraph in paragraphs if paragraph.strip()
                ]
                full_text.extend(formatted_paragraphs)
        self.text = "\n\n".join(full_text)  # Join paragraphs with double newlines
        return self.text

    def save_text_to_file(self, output_file):
        """
        Saves the extracted text to a .txt file.
        """
        if self.text is None:
            raise ValueError("No text extracted. Call `extract_text` first.")
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(self.text)

    def create_dataframe(self):
        """
        Creates a DataFrame from the extracted text, splitting it into paragraphs.
        """
        if self.text is None:
            raise ValueError("No text extracted. Call `extract_text` first.")
        paragraphs = self.text.strip().split("\n\n")  # Split by double newlines
        df = pd.DataFrame(paragraphs, columns=["Paragraph"])
        return df

    def save_dataframe_to_csv(self, df, csv_file):
        """
        Saves the DataFrame to a CSV file.
        """
        df.to_csv(csv_file, index=False, encoding="utf-8")  # Save to CSV

# Usage example
if __name__ == "__main__":
    # File paths
    pdf_path = r"data\MLBOOK.pdf"  # Replace with your PDF file path
    output_txt_file = r"data\extracted_text5.txt"
    output_csv_file = r"data\extracted_text5.csv"

    # Create an instance of PDFTextExtractor
    extractor = PDFTextExtractor(pdf_path)

    # Extract text
    text = extractor.extract_text()

    # Save text to file
    extractor.save_text_to_file(output_txt_file)

    # Create DataFrame
    df = extractor.create_dataframe()

    # Save DataFrame to CSV
    extractor.save_dataframe_to_csv(df, output_csv_file)

    print(f"Extracted text saved to {output_txt_file} and DataFrame saved to {output_csv_file}")
