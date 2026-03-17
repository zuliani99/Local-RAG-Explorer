from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama

# 1. Caricamento Documento
loader = PyPDFLoader("doc/dociment.pdf")
docs = loader.load()

# 2. Divisione in pezzi (Chunking)
# Dividiamo il testo in pezzi da 500 caratteri per non "confondere" l'IA
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

# 3. Creazione Vector Store (Database di conoscenza)
# Usiamo Ollama anche per creare gli "Embeddings" (le impronte digitali del testo)
embeddings = OllamaEmbeddings(model="smollm:1.7b")
vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)

# 4. Creazione della Chain RAG
# 4. Creazione del Retriever e del modello
llm = ChatOllama(model="smollm:1.7b")
retriever = vectorstore.as_retriever()

# 5. Interrogazione
query = "Cosa dice questo documento riguardo al meccanismo dell'attenzione come funziona?"
retrieved_docs = retriever.invoke(query)
context = "\n\n".join(doc.page_content for doc in retrieved_docs)

prompt = f"""Usa esclusivamente il contesto seguente per rispondere alla domanda.

Contesto:
{context}

Domanda:
{query}
"""

risposta = llm.invoke(prompt)

print("\n--- RISPOSTA BASATA SUL TUO PDF ---")
print(risposta.content)