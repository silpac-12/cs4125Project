from sklearn.ensemble import RandomForestClassifier
from models.base_classifier import Classifier

class RandomForestModel(Classifier):
    def __init__(self, n_estimators=100):
        self.model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)
