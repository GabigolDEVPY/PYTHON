from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_NOVA = PASTA_RAIZ / "PDFS"
PASTA_NOVA.mkdir(exist_ok=True)
MEU_PDF = PASTA_RAIZ / "extrato.pdf"

reader = PdfReader(MEU_PDF)
por_image = convert_from_path(MEU_PDF, poppler_path=r"E:\WINDOWS\PROGRAMACAO_TUDO\PYTHON\TODOS\AULAS\pyPDF2\poppler-25.07.0\Library\bin")

page1 = reader.pages[0]
texto_page1 = page1.extract_text()


for i, img in enumerate(por_image):
    texto = pytesseract.image_to_string(img, lang="por")
    print(texto)

