from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_file_path: str, persist_directory: str="./chroma_db"):
        self.csv_file_path = csv_file_path
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
    def build_and_save_vectorstore(self):
        # Load data from CSV
        loader = CSVLoader(
            file_path=self.csv_file_path,
            encoding='utf-8',
            metadata_columns=[]
        )
        
        documents = loader.load()
        
        splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=0
        )
        
        docs = splitter.split_documents(documents)
        
        # Create and persist the vector store
        db = Chroma.from_documents(
            documents=docs,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        
    def load_vector_store(self):
        return Chroma(
            self.persist_directory,
            embedding_function=self.embeddings
        )
