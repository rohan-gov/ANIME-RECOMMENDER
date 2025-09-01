from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import FIREWORKS_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommenderPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            logger.info("Initializing Vector Store Builder")
            
            # create vector store builder instance
            vector_store_builder = VectorStoreBuilder(
                csv_file_path="",
                persist_directory=persist_dir
            )
            
            retriever = vector_store_builder.load_vector_store().as_retriever()
            
            self.recommender = AnimeRecommender(
                retriever=retriever,
                api_key=FIREWORKS_API_KEY,
                model_name=MODEL_NAME
            )
            logger.info("Anime Recommender Pipeline initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing Anime Recommender Pipeline: {e}")
            raise CustomException(e)

    def recommendations(self, query: str) -> str:
        try:
            logger.info(f"Getting recommendations for query: {query}")
            recommendations = self.recommender.get_recommendations(query)
            logger.info("Recommendations retrieved successfully")
            return recommendations
        except Exception as e:
            logger.error(f"Error getting recommendations: {e}")
            raise CustomException(e)
