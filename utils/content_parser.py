from .file_handler import extract_text_from_pdf, extract_text_from_docx, extract_text_from_excel
from .url_utils import fetch_file_from_url, is_pdf, is_docx, is_excel

def parse_content_from_url(url):
    content, content_type = fetch_file_from_url(url)
    if content:
        if is_pdf(content_type):
            return extract_text_from_pdf(content)
        elif is_docx(url):
            return extract_text_from_docx(content)
        elif is_excel(content_type):
            return extract_text_from_excel(content)
        else:
            return "Unsupported file format."
    else:
        return "Failed to fetch the content."
