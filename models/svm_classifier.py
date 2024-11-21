from sklearn.svm import SVC
from models.base_classifier import Classifier

class SVMModel(Classifier):
    def __init__(self):
        self.model = SVC(probability=True)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)
