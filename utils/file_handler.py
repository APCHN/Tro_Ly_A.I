import fitz  # PyMuPDF
from io import BytesIO
from docx import Document
from bs4 import BeautifulSoup
import pandas as pd

def extract_text_from_pdf(pdf_content):
    text = ""
    try:
        pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def extract_text_from_docx(docx_content):
    text = ""
    try:
        doc = Document(BytesIO(docx_content))
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX: {e}")
    return text

def extract_text_from_excel(excel_content):
    try:
        excel_data = pd.read_excel(BytesIO(excel_content), sheet_name=None)
        extracted_text = ""
        for sheet_name, sheet_data in excel_data.items():
            extracted_text += f"Sheet: {sheet_name}\n"
            extracted_text += sheet_data.to_string(index=False)
            extracted_text += "\n\n"
        return extracted_text
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return "Unable to read Excel content."

