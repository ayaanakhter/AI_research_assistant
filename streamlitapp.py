import streamlit as st
import fitz  # PyMuPDF
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Load embedding model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load summarization pipeline
summarizer = pipeline('summarization', model="sshleifer/distilbart-cnn-12-6", device=-1)

# Initialize FAISS index
embedding_dim = 384  # for all-MiniLM-L6-v2
index = faiss.IndexFlatL2(embedding_dim)
documents = []

# Upload and Process PDF
st.title("📚 AI Research Paper Assistant")
st.write("Upload a PDF and ask questions!")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()

    # Break text into smaller chunks
    sentences = text.split('. ')
    chunk_size = 5  # number of sentences per chunk
    chunks = ['. '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]

    # Create embeddings and add to FAISS
    embeddings = embed_model.encode(chunks)
    index.add(np.array(embeddings))
    documents = chunks

    st.success("PDF processed and indexed!")

# Question Answering
query = st.text_input("Ask a question about the document:")

if query and len(documents) > 0:
    # Search FAISS
    query_embedding = embed_model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k=3)

    # Retrieve top chunks
    retrieved_chunks = [documents[i] for i in indices[0]]

    # Summarize the retrieved chunks
    context = " ".join(retrieved_chunks)
    if len(context) > 1000:
        context = context[:1000]  # summarizer has a token limit

    summary = summarizer(context, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

    st.subheader("Answer:")
    st.write(summary)
