import os
import json

TXT_DIR = 'datatxt'
CHUNKS_DIR = 'datachunks'
os.makedirs(CHUNKS_DIR, exist_ok=True)

CHUNK_SIZE = 500
OVERLAP = 100

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

if __name__ == '__main__':
    for fname in os.listdir(TXT_DIR):
        if fname.endswith('.txt'):
            with open(os.path.join(TXT_DIR, fname), 'r', encoding='utf-8') as f:
                text = f.read()
            chunks = chunk_text(text)
            out_path = os.path.join(CHUNKS_DIR, fname.replace('.txt', '.json'))
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump([{'chunk': c} for c in chunks], f, ensure_ascii=False, indent=2)
            print(f'Chunked: {fname} -> {out_path}') 