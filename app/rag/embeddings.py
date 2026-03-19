from langchain_huggingface import HuggingFaceEmbeddings

class EmbeddingModel:
    """
    A wrapper around HuggingFace's embedding model to generate vector representations of text.
    """
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.embedding_model = HuggingFaceEmbeddings(model_name=model_name)
        
    def __call__(self, query: str) -> list:
        return self.embed_query(query)
        
        
    def embed_documents(self, texts: list) -> list:
        """
        Generates embeddings for a list of texts.
        """
        return self.embedding_model.embed_documents(texts)
    
    
    def embed_query(self, query: str) -> list:
        """
        Generates an embedding for a single query string.
        """
        return self.embedding_model.embed_query(query)