from fastapi import FastAPI
import requests

app = FastAPI()

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon"

@app.get("/")
def root():
    return {"message": "Pokémon API Service is running!"}

@app.get("/pokemon/{name}")
def get_pokemon(name: str):
    """Fetch Pokémon details from PokéAPI."""
    response = requests.get(f"{POKEAPI_URL}/{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "base_experience": data["base_experience"],
            "types": [t["type"]["name"] for t in data["types"]]
        }
    return {"error": "Pokémon not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
