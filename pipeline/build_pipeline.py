from src.vector_store import VectorStoreBuilder
from src.data_loader import AnimeDataLoader
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting the build pipeline")
        
        loader = AnimeDataLoader(
            original_file_path="data/anime_with_synopsis.csv",
            processed_file_path="data/processed_anime.csv"
        )
        
        processed_file_path = loader.load_and_process_data()
        
        logger.info("Data loaded and processed successfully")
        
        vector_store_builder = VectorStoreBuilder(
            csv_file_path=processed_file_path,
            persist_directory="chroma_db"
        )
        
        vector_store_builder.build_and_save_vectorstore()
        logger.info("Vector store built and saved successfully")
    except Exception as e:
        logger.error(f"Error in build pipeline: {e}")
        raise CustomException(e)
    
if __name__ == "__main__":
    main()