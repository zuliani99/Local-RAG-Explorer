from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# 1. Inizializza il modello locale
# Assicurati che Ollama sia aperto sul tuo PC
llm = ChatOllama(model="llama3.2", temperature=0.7)

print("--- TEST LOCALE: Ollama + LangChain ---")
template_testo = """
Sei un pirata informatico esperto. 
Spiega cos'è {tecnologia} usando lo slang da pirata.
"""

prompt = PromptTemplate.from_template(template_testo)

# La logica della catena rimane identica! 
# Questo è il bello di LangChain: cambi il modello ma il codice resta uguale.
catena = prompt | llm

# Esecuzione
try:
    risposta = catena.invoke({"tecnologia": "Kubernetes"})
    print(f"Pirata AI: {risposta.content}")
except Exception as e:
    print(f"Errore: Assicurati che Ollama sia avviato! \n{e}")