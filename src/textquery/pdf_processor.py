from typing import Iterator
import PyPDF2
from io import BytesIO

def extract_text_from_pdf(pdf_file) -> str:
    """Extract text content from a PDF file."""
    reader = PyPDF2.PdfReader(BytesIO(pdf_file.read()) if hasattr(pdf_file, 'read') else pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    return text

def chunk_text(text: str, chunk_size: int = 512) -> Iterator[str]:
    """Split text into smaller chunks."""
    words = text.split()
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size]).strip()
        if chunk:
            yield chunk

def process_pdf_file(file, cleaner, embedding_generator, db):
    """Process a single PDF file and store in database."""
    # Extract text from PDF
    text = extract_text_from_pdf(file)
    
    # Clean the text
    clean_text = cleaner.clean_text(text)
    
    # Split into chunks
    chunks = list(chunk_text(clean_text))
    
    # Generate embeddings and store in database
    for chunk in chunks:
        embedding = embedding_generator.encode(chunk)
        db.insert_document(
            title=getattr(file, 'name', 'unknown'),
            body=chunk,
            vector=embedding
        )