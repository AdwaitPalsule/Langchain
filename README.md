
---

## 🤖 Chatbot Module

### Features:
- `app.py`: Uses the OpenAI API for chatbot interactions.
- `localollama.py`: Uses Ollama to run a local LLaMA3.2 model for offline or local inference.

> ⚙️ Ideal for users who want to switch between cloud-based and local LLMs easily.

---

## 📚 RAG module

### Features:
- Simple implementation of a RAG pipeline.
- Uses ChromaDB for vector storage and retrieval.
- Supports both:
  - **Ollama Embeddings**
  - **HuggingFace Embeddings**
- `simplerag.ipynb` shows how to index and retrieve from a knowledge base.

> 📝 Includes `attention.pdf` and `speech.txt` as source documents for retrieval.

---
##🔗 Chain Module
###Features:
- Advanced retrieval-augmented generation (RAG) system.

- Uses Hugging Face embeddings (sentence-transformers/all-mpnet-base-v2).

- Stores and searches vectors using FAISS for fast retrieval.

- Uses a custom prompt template with {context} and {input} — automatically handled by LangChain.

- 'retriever.ipynb' demonstrates full pipeline from query to response.



## 📦 Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-directory>
