from main.preprocess_app_gallery import AppGalleryProcessor
from main.preprocess_purchasing import PurchasingProcessor

if __name__ == "__main__":
    # Process AppGallery Dataset
    app_gallery_processor = AppGalleryProcessor()
    app_gallery_processor.process("data/AppGallery.csv", "data/AppGallery_cleaned.csv")

    # Process Purchasing Dataset
    purchasing_processor = PurchasingProcessor()
    purchasing_processor.process("data/Purchasing.csv", "data/Purchasing_cleaned.csv")
