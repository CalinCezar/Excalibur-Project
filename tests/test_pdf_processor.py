import pytest
from textquery.pdf_processor import chunk_text

def test_chunk_text():
    text = "This is a test text that should be split into chunks"
    chunks = list(chunk_text(text, chunk_size=3))
    assert len(chunks) > 1
    assert all(len(chunk.split()) <= 3 for chunk in chunks)

def test_empty_text_chunking():
    text = ""
    chunks = list(chunk_text(text))
    assert len(chunks) == 0