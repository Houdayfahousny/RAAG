import numpy as np
from sentence_transformers import SentenceTransformer

def search_similar(question, model, index, chunks, k=3):
    q_emb = model.encode([question])
    D, I = index.search(np.array(q_emb), k)
    results = [chunks[i] for i in I[0]]
    return results 