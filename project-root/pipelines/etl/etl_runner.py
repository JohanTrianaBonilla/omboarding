import os
from extract import extract_text_from_pdf
from transform import transform
from load import load
from dotenv import load_dotenv

load_dotenv()

PDF_FOLDER = os.getenv("PDF_FOLDER")

def run_etl():
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]
    print(f"Encontrados {len(pdf_files)} PDFs.\n")

    for pdf in pdf_files:
        print(f"Procesando: {pdf}")

        text = extract_text_from_pdf(f"{PDF_FOLDER}/{pdf}")
        transformed = transform(text)
        result = load(transformed)

        print(f"→ Candidato cargado con ID {result['id']}")
        print(f"→ Embedding creado: {result['embedding']}\n")

if __name__ == "__main__":
    run_etl()
