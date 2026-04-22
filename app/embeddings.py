from sentence_transformers import SentenceTransformer

# load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def recipe_to_text(recipe):
    return f"""
    Name: {recipe['name']}
    Coffee: {recipe['coffee']}
    Water: {recipe['water']}
    Grind: {recipe['grind']}
    Time: {recipe['time']}
    Steps: {recipe['steps']}
    Notes: {recipe['notes']}
    """


def generate_embeddings(recipes):
    texts = [recipe_to_text(r) for r in recipes]
    embeddings = model.encode(texts)
    return embeddings, texts