import requests

base_url ="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}pokemon/{name}"
    return requests.get(url)

pokemon_name = "pikachu"
responce = get_pokemon_info(pokemon_name).json()
print(responce['abilities'])