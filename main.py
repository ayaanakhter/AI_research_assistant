from pdf_text_extractor import extract_text
from text_splitting_code import text_splitting
from embedding_code import create_embeddings
from vector import create_faiss_index
from retriever_code import search_faiss

from sentence_transformers import SentenceTransformer

# Step 1: Load model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 2: Extract text
text = extract_text(r"C:\Users\ayaan\Downloads\demo.pdf")

# Step 3: Split text
chunks = text_splitting(text)

# Step 4: Create embeddings
embeddings = create_embeddings(chunks)

# Step 5: Create FAISS index
index = create_faiss_index(embeddings)

# Step 6: Ask a question
query = input("Ask your question: ")

# Step 7: Search similar chunks
indices = search_faiss(index, query, embed_model)

# Step 8: Show results
for idx in indices[0]:
    print("\nMost Relevant Chunk:")
    print(chunks[idx])
