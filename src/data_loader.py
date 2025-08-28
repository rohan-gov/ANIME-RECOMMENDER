import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_file_path: str, processed_file_path: str):
        self.original_file_path = original_file_path
        self.processed_file_path = processed_file_path
        
    def load_and_process_data(self):
        # Load the original CSV file
        df = pd.read_csv(self.original_file_path, encoding='utf-8', error_bad_lines=False).dropna()
        
        required_columns = ['Name', 'Genres', 'sypnopsis']
        
        missing_columns = required_columns - set(df.columns)
        
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        
        df['combined_info'] = (
            "Title: " + df['Name'] + " Overview: " + df['sypnopsis'] + " Genres: " + df['Genres']
        )
        
        df[['combined_info']].to_csv(self.processed_file_path, index=False, encoding='utf-8')
        
        return self.processed_file_path