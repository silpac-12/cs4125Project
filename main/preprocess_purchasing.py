import pandas as pd
from factories.preprocessor_factory import PreprocessorFactory

class PurchasingProcessor:
    def process(self, input_file, output_file):
        df = pd.read_csv(input_file)
        preprocessor = PreprocessorFactory.get_preprocessor("Purchasing")
        processed_df = preprocessor.preprocess(df)
        processed_df.to_csv(output_file, index=False)
        print(f"Processed Purchasing data saved to {output_file}")
