import streamlit as st
from pathlib import Path
from sentence_transformers import SentenceTransformer
from textquery.cleaner import TextCleaner
from textquery.database import WeaviateDB
from textquery.pdf_processor import process_pdf_file
from textquery.question_generator import QuestionGenerator
from textquery.translator import Translator


st.title("Document Query and Question Generator")

# Initialize components
db = WeaviateDB()
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
cleaner = TextCleaner()
translator = Translator()
question_gen = QuestionGenerator()

# Sidebar for file upload and processing
with st.sidebar:
    st.header("Document Upload")
    uploaded_files = st.file_uploader(
        "Upload PDF documents",
        type="pdf",
        accept_multiple_files=True
    )
    
    if uploaded_files:
        process_button = st.button("Process Documents")
        if process_button:
            progress_bar = st.progress(0)
            for i, file in enumerate(uploaded_files):
                process_pdf_file(
                    file,
                    cleaner,
                    embedding_model,
                    db
                )
                progress_bar.progress((i + 1) / len(uploaded_files))
            st.success("Documents processed successfully!")

# Main area for querying and generating questions
st.header("Query Documents")
query = st.text_input("Enter your query:")

if query:
    with st.spinner("Searching documents..."):
        # Get relevant chunks
        chunks = db.query_similar(query)
        
        if chunks:
            st.subheader("Retrieved Content")
            for i, chunk in enumerate(chunks, 1):
                st.text_area(f"Chunk {i}", chunk, height=100)
            
            if st.button("Generate Questions"):
                with st.spinner("Generating questions..."):
                    # Translate chunks to English
                    en_chunks = [translator.to_english(chunk) for chunk in chunks]
                    
                    # Generate questions
                    questions = []
                    for chunk in en_chunks:
                        chunk_questions = question_gen.generate(chunk)
                        questions.extend(chunk_questions)
                    
                    # Translate questions back to Romanian
                    ro_questions = [translator.to_romanian(q) for q in questions]
                    
                    st.subheader("Generated Questions")
                    for i, question in enumerate(ro_questions, 1):
                        st.write(f"{i}. {question}")
        else:
            st.warning("No relevant documents found for your query.")
