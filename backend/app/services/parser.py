from pathlib import Path
from pypdf import PdfReader
from docx import Document

class ParserService:
    @staticmethod
    def extract_text(file_path: str) -> str:
        """
        Extracts text from a given file (PDF or DOCX).

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The extracted text.
        """
        extension = Path(file_path).suffix.lower()

        if extension == '.pdf':
            return ParserService._read_pdf(file_path)
        elif extension == '.docx':
            return ParserService._read_docx(file_path)
        else:
            raise ValueError(f"Unsupported file format: {extension}")


    @staticmethod
    def _read_pdf(file_path: str) -> str:
        """
        Reads text from a PDF file.

        Args:
            file_path (str): The path to the PDF file.  
            """
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            extracted= page.extract_text() or ""
            if extracted:
                text += extracted + "\n"    
        return text

    @staticmethod
    def _read_docx(file_path: str) -> str:
        """
        Reads text from a DOCX file.

        Args:
            file_path (str): The path to the DOCX file. 
            """
        document = Document(file_path)

        return "\n".join(
            paragraph.text 
            for paragraph in document.paragraphs)


   


    