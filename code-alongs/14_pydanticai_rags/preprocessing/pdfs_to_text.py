from pypdf import PdfReader
from constants import DATA_PATH

def extract_text_from_pdf(path):
    
    all_text = ""
    
    reader = PdfReader(path)

    for page in reader.pages:
        text = page.extract_text()

        all_text += text + "\n"

    return all_text

def export_text(text, export_path):
    with open(export_path, "w") as file:
        file.write(text)

if __name__ == "__main__":
    for pdf_path in DATA_PATH.glob("*.pdf"):
        pdf_text = extract_text_from_pdf(pdf_path)

        filename = f"{pdf_path.stem.casefold()}.txt"

        txt_path = DATA_PATH / filename

        export_text(pdf_text, txt_path)