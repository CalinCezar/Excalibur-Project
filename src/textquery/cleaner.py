from typing import List
import re

class TextCleaner:
    """Class for cleaning and processing text content."""
    
    def __init__(self) -> None:
        self.ignore_sections: List[str] = [
            'Noţiuni-cheie:',
            'Află mai mult',
            'Amintește-ți',
            'Diversitatea lumii vii',
            'activităţi de autoevaluare',
            'exerciții de autoevaluare',
            'Răspunde la întrebări',
            'Completează pe caiet'
            'Ştiai că…?',
        ]
        
        self.ignore_patterns: List[str] = [
            r'^[IVX]+_',
            r'\.pdf$',
            r'^CZU \d+',
            r'^ISBN \d+',
            r'^\d+$',
            r'^Capitolul\s+[IVX]+',
            r'Fig\.\s*\d+',
            r'fig\.\s*\d+',
            r'^\d+\s*\.',
            r'^[a-z]\s*[–-]\s*',
            r'Desenează',
            r'unește prin săgeţi',
            r'a\s*c\s*t\s*i\s*v\s*i\s*t',
            r'.*\b(exercițiu|exercitiu)\b.*',
            r'^[a-z]\s*[–\-)\.]?\s*'
        ]

    def should_ignore_line(self, line: str) -> bool:
        """Check if a line should be ignored."""
        if any(section.lower() in line.lower() for section in self.ignore_sections):
            return True
        
        if any(re.search(pattern, line.strip()) for pattern in self.ignore_patterns):
            return True
            
        if re.match(r'^[\s\d\.\-–,;:]+$', line.strip()):
            return True
            
        return False

    def fix_hyphenated_words(self, text: str) -> str:
        """Fix hyphenated words in text."""
        text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
        text = re.sub(r'(\w+)\s*-\s*(\w+)', r'\1\2', text)
        return text

    def clean_text(self, text: str) -> str:
        """Process and clean text content."""
        lines = [line.strip() for line in text.split('\n')
                if line.strip() and not self.should_ignore_line(line)]
        
        text = '\n'.join(lines)
        text = self.fix_hyphenated_words(text)
        
        # Clean formatting
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\s*\.\s*', '. ', text)
        text = re.sub(r'\s*,\s*', ', ', text)
        text = re.sub(r'\(\s+', '(', text)
        text = re.sub(r'\s+\)', ')', text)
        
        return text.strip()