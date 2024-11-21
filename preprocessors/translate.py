from googletrans import Translator

from config.ConfigManager import ConfigManager
from preprocessors.base_preprocessor import PreprocessorBase


class LanguageTranslationPreprocessor(PreprocessorBase):
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self.translator = Translator()

    def preprocess(self, df):
        df = self._wrapped.preprocess(df)
        # Translate non-English text to English
        def translate_text(text):
            try:
                return self.translator.translate(text, dest=ConfigManager().config["language"]).text
            except:
                return text  # Return the original text if translation fails

        df["cleaned_text"] = df["cleaned_text"].apply(translate_text)
        return df