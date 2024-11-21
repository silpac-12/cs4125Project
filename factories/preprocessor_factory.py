# Factory Pattern: Preprocessor Factory
from preprocessors.base_preprocessor import PreprocessorBase
from preprocessors.noise_removal import NoiseRemovalPreprocessor
from preprocessors.translate import LanguageTranslationPreprocessor


class PreprocessorFactory:
    @staticmethod
    def get_preprocessor(dataset_type):
        if dataset_type == "AppGallery":
            return LanguageTranslationPreprocessor(NoiseRemovalPreprocessor(PreprocessorBase()))
        elif dataset_type == "Purchasing":
            return NoiseRemovalPreprocessor(PreprocessorBase())
        else:
            raise ValueError(f"Unknown dataset type: {dataset_type}")