import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)
st.markdown("""
<style>
    /* Existing styles */
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    .stTextInput textarea {
        color: #ffffff !important;
        background-color: #333333 !important;
        border: 1px solid #555555 !important;
        padding: 8px;
        border-radius: 5px;
    }

    /* Select box styles */
    .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        background-color: #3d3d3d !important;
        padding: 8px;
        border-radius: 5px;
    }

    .stSelectbox svg {
        fill: white !important;
    }

    .stSelectbox option {
        background-color: #2d2d2d !important;
        color: white !important;
    }

    /* Dropdown menu items */
    div[role="listbox"] div {
        background-color: #2d2d2d !important;
        color: white !important;
    }

    /* Focus effect */
    .stTextInput textarea:focus, .stSelectbox div[data-baseweb="select"]:focus {
        border-color: #4CAF50 !important;
        box-shadow: 0 0 5px rgba(76, 175, 80, 0.6);
    }

    /* Hover effects */
    .stSelectbox div[data-baseweb="select"]:hover {
        background-color: #444444 !important;
    }
    div[role="listbox"] div:hover {
        background-color: #444444 !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 DeepSeek Assistant")
st.caption("🚀 Empowering your search with intelligent insights and streamlined solutions.")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Model Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b","deepseek-r1:8b"],
        index=0
    )
    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("""
        - 🐍 Python Expert
        - 🐞 Debugging Assistant
        - 📝 Code Documentation
        - 💡 Solution Design
        - 🔧 Tool Integration
        - 📈 Data Analysis & Visualization
        - ⚙️ Automation & Scripting
    """)

    st.divider()
    st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")


# initiate the chat engine

llm_engine=ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",

    temperature=0.3

)

# System prompt configuration
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI reasoning, coding assistant."
    "Provide concise, accurate solutions with strategic print statements for debugging." 
    "Always communicate in clear, professional English."

)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Greetings! DeepSeek at your service. Ready to help with your reasoning, coding challenges! 🧑‍💻"}]

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input and processing
user_query = st.chat_input("Type your question here...")

def generate_ai_response(prompt_chain):
    processing_pipeline=prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

if user_query:
    # Add user message to log
    st.session_state.message_log.append({"role": "user", "content": user_query})
    
    # Generate AI response
    with st.spinner("🔍 Analyzing..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)
    
    # Add AI response to log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
    # Rerun to update chat display
    st.rerun()