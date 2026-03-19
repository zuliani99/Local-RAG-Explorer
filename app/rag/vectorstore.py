from langchain_community.vectorstores import FAISS

class VectorStore:
    """
    A wrapper around FAISS to store and retrieve vector embeddings for documents.
    """
    
    def __init__(self, embedding):
        self.embedding = embedding
        self.vector_store = None
        
    def create_vector_store(self, texts: list):
        self.vector_store = FAISS.from_texts(texts, self.embedding)
        
        
    def query_vector_store(self, query: str, top_k: int = 5) -> list:
        """
        Queries the vector store with a given query string and returns the top_k most relevant documents.
        """
        if self.vector_store is None:
            raise ValueError("Vector store has not been created. Please call create_vector_store() first.")
    
        docs = self.vector_store.similarity_search(query, k=top_k)
        return [doc.page_content for doc in docs]