from pypdf import PdfReader
from pathlib import Path

class PDFLoader:
    """
    Used only for loading text from the odf file
    """
    
    def __init__(self, pdf_path: Path):
        if not pdf_path.is_file():
            raise FileNotFoundError(f"PDF file not found at {pdf_path}")
        self.pdf_path = pdf_path
        
    def load(self) -> str:
        """
        Reads the PDF file and returns its content as a single string.
        """
        reader = PdfReader(self.pdf_path)
        text = "".join(page.extract_text() + "\n" for page in reader.pages)
        return text.strip()