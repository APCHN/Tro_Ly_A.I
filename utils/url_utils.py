import requests

def fetch_file_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', '')
        return response.content, content_type
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the file: {e}")
        return None, None

def is_pdf(content_type):
    return 'application/pdf' in content_type

def is_docx(url):
    return url.endswith('.docx')

def is_excel(content_type):
    return 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in content_type or 'application/vnd.ms-excel' in content_type
