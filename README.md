
# DeepSeek AI Assistant and RAG System

## Overview

This repository contains two powerful AI-driven applications:

1. **DeepSeek AI Assistant** 🤖 - A Streamlit-based chat assistant powered by LangChain and Ollama, designed to help users with various tasks, including debugging, coding challenges, solution design, and more.
2. **AI-Powered Retrieval-Augmented Generation (RAG) System** 📚 - A document processing and question-answering system that uses PDFs, semantic chunking, embeddings, FAISS for vector storage, and dynamic model selection to answer questions based on document contents.

Both applications leverage Ollama and LangChain to provide intelligent insights and solutions.

---

## Features

### DeepSeek AI Assistant 🤖

- Choose between two powerful models: `deepseek-r1:1.5b` and `deepseek-r1:8b` ⚙️
- Ask coding and reasoning questions 💬
- Receive concise, accurate solutions with debugging print statements 🔍
- Built using LangChain for smooth AI interaction and custom system prompts 🔧

### AI-Powered RAG System 📚

- Upload PDF documents for smart processing 📄
- Text splitting and chunking using semantic embeddings 🧠
- FAISS-based vector storage for efficient retrieval 🚀
- Answer queries related to your documents with model-powered insights 🔎
- Seamlessly integrate different AI models for dynamic document understanding 🧩

---

## Technologies Used 🛠️

- **LangChain**: A framework for building LLM applications with chains, prompts, and agents.
- **Ollama**: Powerful language model integration for task execution.
- **Streamlit**: Interactive front-end interface for chat and document querying.
- **FAISS**: Fast retrieval of relevant document chunks based on query similarity.
- **PDFPlumber**: Used to extract and load PDF content.

---

## Installation 🛠️

### Prerequisites 📋

Make sure you have the following installed:

- Python 3.8+
- Streamlit
- LangChain
- Ollama (ensure Ollama server is running locally)
- FAISS
- Hugging Face Transformers

### Installation Steps ⚙️

1. Clone the repository:
    ```bash
    git clone https://github.com/Prathapmahi/Deepseek-R1-AI.git
    cd DeepSeek-AI
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure Ollama is installed and running on your local machine:
    ```bash
    ollama serve --model deepseek-r1:1.5b  # or deepseek-r1:8b based on selection
    ```

---

## Usage 🖥️

### DeepSeek AI Assistant 🤖

1. Run the Streamlit app:
    ```bash
    streamlit run deepseek_assistant.py
    ```
2. Open the app in your browser and interact with the assistant. You can ask for debugging help, coding solutions, or general queries.

### AI-Powered RAG System 📚

1. Run the Streamlit app:
    ```bash
    streamlit run rag_system.py
    ```
2. Upload a PDF document and ask questions based on the contents. The system will retrieve relevant document chunks and provide insightful answers based on the selected model.

---

## Configuration ⚙️

Both apps allow you to choose between the following models:

- `deepseek-r1:1.5b`
- `deepseek-r1:8b`

Select the model that best fits your task.

---

## Additional Notes 📝

- Ensure your PDF files are well-formatted for best results with the RAG system 📄.
- The assistant is designed for general-purpose tasks and can be fine-tuned for more specific needs 🧑‍💻.
- If you encounter any issues with the app, please refer to the documentation or open an issue in the repository 🚨.

---

## Contributing 🤝

We welcome contributions! Feel free to fork the repository, submit pull requests, and suggest improvements. If you find bugs or have feature requests, please open an issue.

---

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments 🙏

- **LangChain**: For making it easy to build LLM applications 🧩.
- **Ollama**: For providing powerful AI models 🤖.
- **FAISS**: For efficient document retrieval 🚀.

---

