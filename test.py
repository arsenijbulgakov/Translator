import pytest

from model import TranslateModel


@pytest.fixture()
def translate_model():
    model = TranslateModel()
    yield model


class TestTranslateModel:
    @pytest.mark.parametrize("text", ["a", "b", "hello", "cat", "dog"])
    def test_type(self, translate_model, text):
        translated_text = translate_model.translate(text)
        assert isinstance(translated_text, str)

    @pytest.mark.parametrize("text", ["hello!", "cat", "dog", "bed"])
    def test_en_ru(self, translate_model, text):
        answers = {"hello!": ["привет!", "здравствуй!", "здравствуйте!"], "cat": ["кот", "кошка"], "dog": ["собака"], "bed": ["кровать"]}
        translated_text = translate_model.translate(text)
        assert translated_text.lower() in answers[text]

    @pytest.mark.parametrize("text", ["кот", "собака", "бегать"])
    def test_ru_en(self, translate_model, text):
        answers = {"кот": ["cat"], "собака": ["dog"], "бегать": ["run"]}
        translate_model.change_dst_lang("en")
        translated_text = translate_model.translate(text)
        assert translated_text.lower() in answers[text]
