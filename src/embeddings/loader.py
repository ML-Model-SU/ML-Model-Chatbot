def split_text_into_chunks(file_path, chunk_size=512):
    """
    Splits a large text file into smaller chunks.
    :param file_path: Path to the text file.
    :param chunk_size: Size of each chunk (number of characters).
    :return: List of text chunks.
    """
    with open(file_path, "r", encoding='utf-8') as f:
        text = f.read()
    
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
