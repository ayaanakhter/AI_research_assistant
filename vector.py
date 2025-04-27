import faiss
import numpy as np

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]  # embedding size, usually 384
    index = faiss.IndexFlatL2(dimension)  # L2 distance = normal distance

    index.add(np.array(embeddings))  # Add embeddings to FAISS
    return index
