import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from models.model_factory import ModelFactory

class ModelTrainer:
    def train_and_test(self, app_gallery_path, purchasing_path, model_type):
        # Load cleaned data
        app_gallery_data = pd.read_csv(app_gallery_path)
        purchasing_data = pd.read_csv(purchasing_path)

        # Combine datasets
        data = pd.concat([app_gallery_data, purchasing_data])

        # Ensure 'cleaned_text' does not contain NaN values
        data['cleaned_text'] = data['cleaned_text'].fillna("")

        # Vectorize text
        tfidf = TfidfVectorizer(max_features=2000)
        X = tfidf.fit_transform(data["cleaned_text"]).toarray()
        y = data["Type 1"]  # Replace with your target column

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create model using Factory
        model = ModelFactory.create_model(model_type)

        # Train model
        print(f"Training {model_type} model...")
        model.train(X_train, y_train)

        # Test model
        print(f"Testing {model_type} model...")
        y_pred = model.predict(X_test)

        # Evaluate model
        print(f"Evaluation Report for {model_type} model:")
        print(classification_report(y_test, y_pred))
