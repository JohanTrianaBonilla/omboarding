import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extrae texto de un PDF."""
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"

    return full_text.strip()
