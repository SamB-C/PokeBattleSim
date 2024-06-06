import requests
import json
import random

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

def abilityPicker():
        #Ability Picker
        response_API = requests.get(POKEAPI_BASE_URL + "pokemon/" + pokemon)
        pokemon_info = response_API.text
        #Might put it in a list, acts like a list.
        parse_json = json.loads(pokemon_info)
        querey = parse_json["abilities"]
        #Picks a random ability from the list of abilities it can have.
        random_ability_picker = random.randint(0,len(querey))
        random_ability = querey[random_ability_picker - 1]
        print(pokemon.capitalize(), "has the ability", random_ability["ability"]["name"] + ".")

def pokemonType():
        types = []
        #Pokemon Type Finder
        response_API = requests.get(POKEAPI_BASE_URL + "pokemon/" + pokemon)
        pokemon_info = response_API.text
        #Might put it in a list, acts like a list.
        parse_json = json.loads(pokemon_info)
        querey = parse_json["types"]
        for type in querey:
                types.append(type["type"]["name"])
        if len(types) == 2:
                print(pokemon.capitalize(), "has 2 types:", types[0].capitalize(), "and", types[1].capitalize())
        else:
                print(pokemon.capitalize(), "has 1 type:", types[0].capitalize())

if __name__ == '__main__':
        pokemon = input("Please Enter the Name of a Pokemon\n").lower()
        abilityPicker()
        pokemonType()
    
    
