import streamlit as st
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import RetrievalQA

# Centered Title & Caption
st.markdown(
    """
    <h1 style="text-align: center;">🚀 AI-Powered RAG System with DeepSeek R1 & Ollama</h1>
    """,
    unsafe_allow_html=True
)
st.caption("<p style='text-align: center;'>Ask Anything About Your PDFs – Smart Retrieval Meets Powerful AI! 🔍🤖</p>", unsafe_allow_html=True)

# Sidebar for Model Selection
with st.sidebar:
    st.header("⚙️ Model Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:8b"],  # Allow model selection
        index=1
    )
    st.divider()
    st.markdown("### 🧩 RAG Pipeline 🔍🤖")
    st.markdown("""
        - ✅ Upload PDF 
        - 🔀 Text Splitting 
        - 🧠 Embedding 
        - 📚 FAISS Storage 
        - 🎛 Model Selection 
        - 📜 Prompt Construction 
        - 🔍 Query Processing 
        - 💡 LLM Response   
    """)

# File Upload
uploaded_file = st.file_uploader("📄 Upload your PDF file here", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getvalue())

    # Load and process PDF
    loader = PDFPlumberLoader("temp.pdf")
    docs = loader.load()

    # Split document into meaningful chunks
    text_splitter = SemanticChunker(HuggingFaceEmbeddings())
    documents = text_splitter.split_documents(docs)

    # Embedding & Vector Storage
    embedder = HuggingFaceEmbeddings()
    vector = FAISS.from_documents(documents, embedder)
    retriever = vector.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    # Load selected model dynamically
    llm = Ollama(model=selected_model)

    # Prompt Template
    prompt = """
    Use the following context to answer the question.
    Context: {context}
    Question: {question}
    Answer:"""

    QA_PROMPT = PromptTemplate.from_template(prompt)

    # LLM Chain
    llm_chain = LLMChain(llm=llm, prompt=QA_PROMPT)
    combine_documents_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="context")

    # Retrieval QA System
    qa = RetrievalQA(combine_documents_chain=combine_documents_chain, retriever=retriever)

    # User Input
    user_input = st.text_input("💬 Ask a question about your document:")

    if user_input:
        with st.spinner("🧠 Processing..."):  # Improved feedback
            response = qa(user_input)["result"]
        st.write("**📝 Response:**")
        st.write(response)
