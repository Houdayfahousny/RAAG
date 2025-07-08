from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os
import numpy as np
import json
from sentence_transformers import SentenceTransformer
import vectordb
from search_engine import search_similar
from llama3_client import call_llama3

EMBED_DIR = 'dataembeddings'
MODEL_NAME = 'all-MiniLM-L6-v2'
K = 3

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

model = SentenceTransformer(MODEL_NAME)

# Charger tous les embeddings et chunks
all_embeddings = []
all_chunks = []
for fname in os.listdir(EMBED_DIR):
    if fname.endswith('_embeddings.npy'):
        base = fname.replace('_embeddings.npy', '')
        emb = np.load(os.path.join(EMBED_DIR, fname))
        with open(os.path.join(EMBED_DIR, base + '_chunks.json'), 'r', encoding='utf-8') as f:
            chunks = json.load(f)
        all_embeddings.append(emb)
        all_chunks.extend(chunks)

if all_embeddings:
    embeddings = np.vstack(all_embeddings)
else:
    embeddings = np.array([])

if embeddings.size == 0:
    raise RuntimeError('Aucun embedding trouvé.')

index = vectordb.build_faiss_index(embeddings)

@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.html")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    question = data.get("question", "")
    passages = search_similar(question, model, index, all_chunks, k=K)
    context = '\n'.join(passages)
    answer = call_llama3(question, context)
    return JSONResponse({"answer": answer, "context": context})
