from pathlib import Path
from pypdf import PdfReader
from docx import Document
from ebooklib import epub
from bs4 import BeautifulSoup
import markdown
import ebooklib

def read_txt(path):
    encodings = ["utf-8", "utf-8-sig", "cp1252", "latin-1"]
    for encoding in encodings:
        try:
            with open(path, encoding = encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise Exception("Could not read text file: {path}")


def read_pdf(path):
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def read_docx(path):
    document = Document(path)
    text = []
    for paragraph in document.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)

def read_epub(path):
    book = epub.read_epub(path)
    text = []

    for item in book.get_items():
        if item.get_name().endswith((".xhtml","html",".htm")):
            soup = BeautifulSoup(item.get_content(), "html.parser")
            text.append(soup.get_text())
    return "\n".join(text)

def read_markdown(path):
    raw_text = read_txt(path)
    html = markdown.markdown(raw_text)
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


def read_html(path):
    raw_html = read_txt(path)
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text()




def read_document(path):
    extension = Path(path).suffix.lower()
    print(repr(extension))
    if extension == ".txt":
        return read_txt(path)
    if extension == ".pdf":
        return read_pdf(path)
    if extension == ".docx":
        return read_docx(path)
    if extension == ".epub":
        return read_epub(path)
    if extension == ".md":
        return read_markdown(path)
    if extension in [".html",".htm"]:
        return read_html(path)
    
    raise Exception(f"Unsupported file type: {extension}")