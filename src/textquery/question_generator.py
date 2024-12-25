from typing import List
from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline

class QuestionGenerator:
    """Generate questions from text using T5 model."""
    
    def __init__(self, model_name: str = "ZhangCheng/T5-Base-Fine-Tuned-for-Question-Generation") -> None:
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.pipeline = pipeline(
            "text2text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
        )
    
    def generate(self, text: str, max_length: int = 128) -> List[str]:
        """Generate questions from text."""
        outputs = self.pipeline(text, max_length=max_length)
        return [output["generated_text"] for output in outputs]