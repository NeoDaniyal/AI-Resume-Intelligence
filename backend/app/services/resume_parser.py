import fitz
from io import BytesIO
from docx import Document

def extract_pdf_text(file_content: bytes) -> str:
    """Extract text from a PDF file using PyMuPDF (fitz)."""
    text = []
    with fitz.open(stream=file_content, filetype="pdf") as pdf_document:
        for page in pdf_document:
            page_text = page.get_text()
            text.append(page_text)
    return "\n".join(text)

def extract_docx_text(file_content: bytes)-> str:
    """Extract text from a Docx documents."""
    document = Document(BytesIO(file_content))

    paragraphs = [paragraph.text for paragraph in document.paragraphs if paragraph.text.strip()]

    for table in document.tables:
        for row in table.rows:
            for cell in table.cells:
                if cell.text.strip():
                    paragraphs.append(cell.text)
    return "\n".join(paragraphs)

def  extract_text(file_content: bytes, extension: str) -> str:
    if extension == ".pdf":
        return extract_pdf_text(file_content)
    elif extension == ".docx":
        return extract_docx_text(file_content)
    else:
        raise ValueError("Unsupported document format.")