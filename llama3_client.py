import os
import requests

# Charger la clé API depuis un fichier .env si présent
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv n'est pas obligatoire mais recommandé

# Récupérer la clé API Groq depuis la variable d'environnement
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY or not GROQ_API_KEY.strip():
    raise ValueError("Veuillez définir la variable d'environnement GROQ_API_KEY (dans .env ou votre shell) avec uniquement la clé, sans préfixe ni retour à la ligne.")
GROQ_API_KEY = GROQ_API_KEY.strip()

# Endpoint Groq compatible OpenAI
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Modèle par défaut (Llama 3 70B)
DEFAULT_MODEL = "llama-3.3-70b-versatile"

# Prompt template pour RAG
PROMPT_TEMPLATE = (
    """
    Tu es un assistant pédagogique expert. Utilise le contexte ci-dessous pour répondre à la question de façon claire, concise et pédagogique.
    Si le contexte ne contient pas la réponse, indique-le honnêtement.

    Contexte :
{context}

    Question : {question}
    Réponse :
    """
)

def call_llama3(question, context, model=DEFAULT_MODEL, temperature=0.2, max_tokens=512):
    """
    Envoie la question et le contexte à Llama 3 70B via l'API Groq (HTTP requests) et retourne la réponse.
    """
    prompt = PROMPT_TEMPLATE.format(context=context, question=question)
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"].strip()

if __name__ == "__main__":
    print("Test CLI Llama 3 70B (Groq, via requests)")
    question = input("Question : ")
    context = input("Contexte (optionnel, laisser vide si aucun) : ")
    answer = call_llama3(question, context)
    print("\n--- Réponse IA ---\n")
    print(answer) 