from fastapi import FastAPI
from app.data_loader import load_recipes
from app.embeddings import generate_embeddings, model
from app.retrieval import create_faiss_index, search

app = FastAPI()

# load once (important)
recipes = load_recipes()
embeddings, texts = generate_embeddings(recipes)
index = create_faiss_index(embeddings)


@app.get("/")
def query_recipes(q: str = "strong coffee"):
    query_embedding = model.encode(q)

    results = search(index, query_embedding)

    matched_recipes = [texts[i] for i in results]

    return {
        "query": q,
        "results": matched_recipes
    }