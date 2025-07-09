# Plateforme e-learning RAG + Llama 3 70B (Groq)

Ce projet est une plateforme e-learning basée sur le Retrieval-Augmented Generation (RAG) avec FastAPI, une interface web interactive, et l'intégration du modèle Llama 3 70B via l'API Groq. Il permet de questionner des documents de formation (PDF) et d'obtenir des réponses enrichies par l'IA.

---

## 🚀 Fonctionnalités
- Extraction automatique du texte depuis des PDF
- Chunking intelligent des documents
- Génération d'embeddings et indexation vectorielle (FAISS)
- Recherche sémantique de passages pertinents
- Orchestration RAG + LLM (Llama 3 70B via Groq)
- Interface web de chat moderne (FastAPI + HTML/CSS/JS)

---

## 📁 Structure du projet

```
Stage/
│
├── app.py                # Serveur FastAPI (chat web)
├── chat.py               # Script CLI pour tester le RAG
├── chunking.py           # Découpage des textes en chunks
├── embed.py              # Génération des embeddings
├── llama3_client.py      # Appel à l'API Groq (LLM)
├── parser.py             # Extraction texte PDF → TXT
├── requirements.txt      # Dépendances Python
├── search_engine.py      # Recherche de similarité
├── vectordb.py           # Gestion de la base vectorielle
│
├── static/
│   └── index.html        # Frontend web (chat)
│
├── data/                 # (Placez vos PDF ici)
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

1. **Cloner le dépôt**
2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate sous Windows
   ```
3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
4. **Obtenir une clé API Groq**
   - Inscrivez-vous sur https://console.groq.com/ et copiez votre clé API.

---

## 🔑 Variables d'environnement

Définissez la clé API Groq avant de lancer le chat :
```bash
# Sous Linux/Mac
export GROQ_API_KEY="votre_cle_groq"
# Sous Windows PowerShell
$env:GROQ_API_KEY="votre_cle_groq"
```

---

## 🛠️ Pipeline d'utilisation

1. **Placez vos PDF dans le dossier `data/`**
2. **Extraction du texte**
   ```bash
   python parser.py
   ```
3. **Découpage en chunks**
   ```bash
   python chunking.py
   ```
4. **Génération des embeddings**
   ```bash
   python embed.py
   ```
5. **Lancer le chat web**
   ```bash
   uvicorn app:app --reload
   # Ouvrez http://localhost:8000 dans votre navigateur
   ```
6. **(Optionnel) Tester en ligne de commande**
   ```bash
   python chat.py
   ```

---

## 💡 Exemple d'utilisation

- Posez une question sur le contenu de vos PDF via l'interface web ou le script CLI.
- L'IA recherche les passages pertinents et génère une réponse pédagogique.

---

## 📝 Personnalisation
- Modifiez `static/index.html` pour adapter le style du chat.
- Adaptez les scripts pour d'autres formats (PPTX, DOCX, etc.).
- Ajoutez des endpoints FastAPI pour l'upload, l'historique, etc.

---

## 🧹 Bonnes pratiques
- **Ne pas versionner** : `venv/`, `dataembeddings/`, `datatxt/`, `datachunks/`, `*.npy`, `*.json` générés, `faiss.index`, etc.
- Utilisez `.gitignore` pour garder le dépôt propre.

---

## 📄 Licence
MIT
