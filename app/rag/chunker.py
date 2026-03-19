from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List

class LangchainTextChunker:
    """
    A wrapper around Langchain's RecursiveCharacterTextSplitter to chunk text into smaller pieces.
    """
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap
        )
        
    def chunk(self, text: str) -> List[str]:
        """
        Splits the input text into chunks based on the specified chunk size and overlap.
        """
        return self.text_splitter.split_text(text)