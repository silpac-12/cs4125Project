from main.preprocess_app_gallery import AppGalleryProcessor
from main.preprocess_purchasing import PurchasingProcessor
from train.train_model import ModelTrainer

if __name__ == "__main__":
    # Step 1: Preprocess AppGallery Dataset
    app_gallery_processor = AppGalleryProcessor()
    app_gallery_processor.process("data/AppGallery.csv", "data/AppGallery_cleaned.csv")

    # Step 2: Preprocess Purchasing Dataset
    purchasing_processor = PurchasingProcessor()
    purchasing_processor.process("data/Purchasing.csv", "data/Purchasing_cleaned.csv")

    # Step 3: Train and Test Model
    model_trainer = ModelTrainer()
    model_trainer.train_and_test(
        app_gallery_path="data/AppGallery_cleaned.csv",
        purchasing_path="data/Purchasing_cleaned.csv",
        model_type="RandomForest"  # Change to "SVM" or other model types as needed
    )
