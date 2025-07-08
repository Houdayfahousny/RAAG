import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNKS_DIR = 'datachunks'
EMBED_DIR = 'dataembeddings'
os.makedirs(EMBED_DIR, exist_ok=True)
MODEL_NAME = 'all-MiniLM-L6-v2'

model = SentenceTransformer(MODEL_NAME)

if __name__ == '__main__':
    for fname in os.listdir(CHUNKS_DIR):
        if fname.endswith('.json'):
            with open(os.path.join(CHUNKS_DIR, fname), 'r', encoding='utf-8') as f:
                data = json.load(f)
            chunks = [item['chunk'] for item in data]
            embeddings = model.encode(chunks, show_progress_bar=True, batch_size=32)
            base = fname.replace('.json', '')
            np.save(os.path.join(EMBED_DIR, base + '_embeddings.npy'), embeddings)
            with open(os.path.join(EMBED_DIR, base + '_chunks.json'), 'w', encoding='utf-8') as f:
                json.dump(chunks, f, ensure_ascii=False, indent=2)
            print(f'Embeddings: {fname} -> {base}_embeddings.npy') 