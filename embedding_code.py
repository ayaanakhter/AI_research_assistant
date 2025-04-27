from sentence_transformers import SentenceTransformer

def create_embeddings(chunks):
    # Load a lightweight, CPU-friendly model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Encode all text chunks into embeddings
    embeddings = model.encode(chunks, show_progress_bar=True)
    
    return embeddings
