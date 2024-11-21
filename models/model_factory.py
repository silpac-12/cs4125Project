from models.random_forest_classifier import RandomForestModel
from models.svm_classifier import SVMModel

class ModelFactory:
    @staticmethod
    def create_model(model_type):
        if model_type == "RandomForest":
            return RandomForestModel()
        elif model_type == "SVM":
            return SVMModel()
        else:
            raise ValueError(f"Unknown model type: {model_type}")
