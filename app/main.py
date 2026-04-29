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

    matched_recipes = [recipes[i] for i in results]

    response_recipes = [{"name": i["name"], "notes": i["notes"]} for i in results]

    context_parts = []

    for recipe in matched_recipes:
        text = f"{recipe['name']}: {recipe['notes']}"
        context_parts.append(text)

    context = "\n".join(context_parts)

    return {
        "query": q,
        "recipes": response_recipes,
        "context": context
    }