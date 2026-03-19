from fastapi import FastAPI, Query
from app.rag.engine import RAGEngine

app = FastAPI()
rag_engine = RAGEngine()

@app.get("/query")
def query(question: str = Query(..., description="User question")):
    """
    Return an LLM generated answer to the user's question based on the context from the PDF document.
    The question is passed as a query parameter, and the response includes both the original question and the generated answer.
    """
    try:
        answer = rag_engine.generate_answer(question)
        
        return {
            "question": question, 
            "answer": answer
        }
    
        
    except Exception as e:
        return {
            "question": question,
            "answer": None,
            "error": str(e)
        }
    
    