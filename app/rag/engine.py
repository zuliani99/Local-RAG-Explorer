from app.core.config import PDF_PATH, CHUNK_SIZE, CHUNK_OVERLAP, EMBEDDING_MODEL, TOP_K
from app.rag.loader import PDFLoader
from app.rag.chunker import LangchainTextChunker
from app.rag.embeddings import EmbeddingModel
from app.rag.vectorstore import VectorStore

from langchain.agents import create_agent
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

class RAGEngine:
    """
    The main engine for the RAG application, responsible for loading documents, creating embeddings, and handling queries.
    """
    
    def __init__(self):
        self.vector_store = None
        self._initialize()
        
    def _initialize(self):
        load_dotenv()
        
        text = PDFLoader(PDF_PATH).load()
        chunker = LangchainTextChunker(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        chunks = chunker.chunk(text)
        embedding_model = EmbeddingModel(model_name=EMBEDDING_MODEL)
        self.vector_store = VectorStore(embedding_model)
        self.vector_store.create_vector_store(chunks)
        self.llm=ChatGroq(model_name="llama-3.3-70b-versatile")
        
    def generate_answer(self, question: str) -> str:
        """
        Generates an answer to a given question by querying the vector store and using the LLM to formulate a response.
        Retreive the top_k chubnks from the vector store based on the question, then use those chunks as context to generate an answer using the LLM.
        """
        relevant_docs = self.vector_store.query_vector_store(question, top_k=TOP_K)
        context = "\n".join(relevant_docs)
        
        prompt_template = f"""
        You are a helpful assistant that answers questions based on the following context from a PDF document. 
        Use the provided context to answer the question as accurately as possible. 
        If the context does not contain enough information to answer the question, say "I don't know."
        
        Context: {context}\n\nQuestion: {question}\nAnswer:
        """
        agent = create_agent(
            model=self.llm,
            system_prompt="You are a helpful assistant."
        )
        
        result = agent.invoke({
            "messages": [{"role": "user", "content": prompt_template}]
        })
        
        return result['messages'][-1].content