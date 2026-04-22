import json

def load_recipes(path="data/recipes.json"):
    with open(path, "r") as f:
        return json.load(f)