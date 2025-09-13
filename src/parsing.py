import pdfplumber
import docx2txt
import os

def extract_text_from_pdf(path: str) -> str:
    text = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def extract_text_from_docx(path: str) -> str:
    return docx2txt.process(path)

def extract_text(path: str) -> str:
    path_lower = path.lower()
    if path_lower.endswith('.pdf'):
        return extract_text_from_pdf(path)
    elif path_lower.endswith('.docx') or path_lower.endswith('.doc'):
        return extract_text_from_docx(path)
    else:
        # fall back: read text file
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except:
            return ''
