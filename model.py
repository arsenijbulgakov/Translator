"""Class for T5 model inference.."""
from transformers import T5ForConditionalGeneration, T5Tokenizer

MODEL_PATH = "utrobinmv/t5_translate_en_ru_zh_small_1024"
AVAILABLE_LANGS = ["en", "ru", "zh"]


class TranslateModel:
    """Model for text translating."""

    def __init__(self, dst_lang="ru"):
        """Set dst language, download vocab and weights for T5 model."""
        self.dst_lang = dst_lang

        self.tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
        self.model = T5ForConditionalGeneration.from_pretrained(
            MODEL_PATH, return_dict=True
        )

    def change_dst_lang(self, lang):
        """Set another dst language."""
        assert lang in AVAILABLE_LANGS
        self.dst_lang = lang

    def translate(self, text):
        """Translate given text."""
        prefix = f"translate to {self.dst_lang}: "
        input_ids = self.tokenizer(prefix + text, return_tensors="pt")
        generated_tokens = self.model.generate(**input_ids)
        result = self.tokenizer.batch_decode(
            generated_tokens, skip_special_tokens=True
        )[0]

        return result
