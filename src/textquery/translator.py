from deep_translator import GoogleTranslator

class Translator:
    """Handle text translation between languages."""
    
    def __init__(self) -> None:
        self.en_translator = GoogleTranslator(source='ro', target='en')
        self.ro_translator = GoogleTranslator(source='en', target='ro')
    
    def to_english(self, text: str) -> str:
        """Translate text from Romanian to English."""
        return self.en_translator.translate(text)
    
    def to_romanian(self, text: str) -> str:
        """Translate text from English to Romanian."""
        return self.ro_translator.translate(text)