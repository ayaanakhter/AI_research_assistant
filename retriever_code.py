import numpy as np

def search_faiss(index, query, embed_model, k=3):
    # 1. Convert query into embedding
    query_embedding = embed_model.encode([query])

    # 2. Search FAISS index for top-k similar embeddings
    distances, indices = index.search(np.array(query_embedding), k)

    return indices
