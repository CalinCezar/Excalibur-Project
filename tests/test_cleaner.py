import pytest
from textquery.cleaner import TextCleaner

def test_should_ignore_line():
    cleaner = TextCleaner()
    assert cleaner.should_ignore_line("Noţiuni-cheie: test") == True
    assert cleaner.should_ignore_line("Normal text") == False
    assert cleaner.should_ignore_line("1. ") == True
    assert cleaner.should_ignore_line("Fig. 1") == True

def test_fix_hyphenated_words():
    cleaner = TextCleaner()
    assert cleaner.fix_hyphenated_words("test-\ning") == "testing"
    assert cleaner.fix_hyphenated_words("test - ing") == "testing"

def test_clean_text():
    cleaner = TextCleaner()
    text = "Test text.\nFig. 1\nNoţiuni-cheie: ignore\nReal content"
    cleaned = cleaner.clean_text(text)
    assert "Fig. 1" not in cleaned
    assert "Noţiuni-cheie:" not in cleaned
    assert "Test text" in cleaned
    assert "Real content" in cleaned

# tests/test_embeddings.py
import pytest
from textquery.embeddings import EmbeddingGenerator

def test_embedding_generation():
    generator = EmbeddingGenerator()
    text = "Test text"
    embedding = generator.generate(text)
    assert isinstance(embedding, list)
    assert all(isinstance(x, float) for x in embedding)

def test_batch_embedding_generation():
    generator = EmbeddingGenerator()
    texts = ["Test text 1", "Test text 2"]
    embeddings = generator.generate_batch(texts)
    assert len(embeddings) == 2
    assert all(isinstance(x, list) for x in embeddings)