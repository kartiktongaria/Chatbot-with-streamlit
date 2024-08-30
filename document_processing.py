import os
from pypdf import PdfReader
from docx import Document
import re

def extract_text_from_pdf_directory(directory_path="documents"):

    text = ""

    for filename in os.listdir(directory_path):
        print("Processing : ", filename)
        file_path = os.path.join(directory_path, filename)
        
        if filename.lower().endswith('.pdf'):
            try:
                pdf_reader = PdfReader(file_path)
                for page in pdf_reader.pages:
                    text += page.extract_text() or ''
            except Exception as e:
                print(f"Error processing {filename}: {e}")

        elif filename.lower().endswith('.docx'):
            try:
                doc = Document(file_path)
                for para in doc.paragraphs:
                    text += para.text + '\n'
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return text


def clean_text(text):
    text = text.strip()
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    
    return text