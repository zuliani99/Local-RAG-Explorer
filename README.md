# Local-RAG Explorer: Full-Stack AI & DevOps Project

A private, secure, and fully orchestrated document assistant built during an intensive 5-day sprint. This project demonstrates the integration of Generative AI with modern Cloud-Native infrastructure.

## 🚀 Key Features
- **Local RAG Pipeline:** Uses LangChain to process PDFs locally, ensuring data privacy.
- **AI Engine:** Powered by Ollama (Llama 3.2 / Smollm) for cost-free, offline inference.
- **Interactive UI:** A clean chat interface built with Streamlit.
- **Containerized:** Fully Dockerized with optimized "slim" images for low-resource environments.
- **Orchestrated:** Deployed and managed via Kubernetes (Kind) for scalability and resilience.

## 🛠️ Tech Stack
- **AI/LLM:** LangChain, Ollama, ChromaDB (Vector Store)
- **Frontend:** Streamlit
- **DevOps:** Docker, Kubernetes (Kind), Kubectl
- **Environment:** Python 3.10-slim

## 💻 Quick Command Reference

### 1. Setup AI (Ollama)
```bash
ollama pull llama3.2              # Download the LLM
ollama list                       # Check available models
```

### 2. Python Environment
```bash
python -m venv rag_env            # Create virtual env
source rag_env/bin/activate       # Activate (Linux)
pip install -r requirements.txt   # Install dependencies
```

### 3. Docker (Packaging)
```bash
docker build -t mio-rag-app .     # Build the image
docker run -p 8501:8501 mio-rag-app # Run container locally
```

### 4. Kubernetes (Orchestration)
```bash
kind create cluster --name mio-rag-cluster         # Create local cluster
kind load docker-image mio-rag-app:latest --name mio-rag-cluster # Load image
kubectl apply -f deployment.yaml                   # Deploy app
kubectl apply -f service.yaml                      # Create service
kubectl get pods -w                                # Monitor status
kubectl port-forward service/rag-ai-service 8501:80 # Access via browser
```

### 5. Cleanup
```bash
kubectl delete -f deployment.yaml                  # Stop the app
kind delete cluster --name mio-rag-cluster         # Delete the cluster
docker system prune                                # Free disk space
```