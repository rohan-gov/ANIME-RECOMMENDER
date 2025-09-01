from langchain.chains import RetrievalQA
from langchain_fireworks import ChatFireworks
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.retriever = retriever
        self.api_key = api_key
        self.model_name = model_name
        self.prompt = get_anime_prompt()
        self.llm = ChatFireworks(api_key=self.api_key, model_name=self.model_name)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )
        
    def get_recommendations(self, query: str):
        result = self.qa_chain({"query": query})
        return result['result']
