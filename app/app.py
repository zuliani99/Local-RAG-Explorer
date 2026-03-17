import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama

from langchain_classic.chains import RetrievalQA

# Configurazione della pagina Streamlit
st.set_page_config(page_title="Il mio RAG Locale", layout="centered")
st.title("🤖 Chatta con i tuoi documenti (Gratis & Locale)")

# Inizializziamo il modello
#llm = ChatOllama(model="llama3.2")
#embeddings = OllamaEmbeddings(model="llama3.2")

llm = ChatOllama(
    model="llama3.2", 
    base_url="http://host.docker.internal:11434" # Questo permette al container di uscire e parlare con il tuo PC
)
embeddings = OllamaEmbeddings(
    model="llama3.2",
    base_url="http://host.docker.internal:11434"
)

# Sidebar per il caricamento del file
with st.sidebar:
    st.header("Carica Documento")
    uploaded_file = st.file_uploader("Scegli un PDF", type="pdf")
    
    if uploaded_file:
        # Salvataggio temporaneo del file per leggerlo
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getvalue())
        
        st.success("File caricato con successo!")
        
        # Logica RAG (Giorno 2)
        loader = PyPDFLoader("temp.pdf")
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(docs)
        
        # Creiamo il database vettoriale in memoria
        vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
        
        # Creiamo la catena di risposta
        st.session_state.rag_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )

# Area della Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra i messaggi precedenti
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dell'utente
if prompt := st.chat_input("Fai una domanda sul documento..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generazione risposta
    with st.chat_message("assistant"):
        if "rag_chain" in st.session_state:
            with st.spinner("Sto leggendo..."):
                response = st.session_state.rag_chain.invoke(prompt)
                full_response = response["result"]
                st.markdown(full_response)
        else:
            full_response = "Per favore, carica prima un PDF nella barra laterale!"
            st.warning(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})