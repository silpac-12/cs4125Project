import re
from preprocessors.base_preprocessor import PreprocessorBase


class NoiseRemovalPreprocessor(PreprocessorBase):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def preprocess(self, df):
        df = self._wrapped.preprocess(df)
        # Remove common noise like email addresses and special characters
        df["cleaned_text"] = df["Interaction content"].apply(lambda x: re.sub(r'[^\w\s]', '', str(x)))
        return df