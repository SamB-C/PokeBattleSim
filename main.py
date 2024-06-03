import requests
import json

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

if __name__ == '__main__':
    pokemon = input("Please enter the name of a pokemon").lower()
    response_API = requests.get(POKEAPI_BASE_URL + "pokemon/" + pokemon)
    pokemon_info = response_API.text
    parse_json = json.loads(pokemon_info)
    querey = parse_json["abilities"]
    print(querey)
