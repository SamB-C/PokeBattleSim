import requests
import json
import random
from tkinter import *
from tkinter import ttk
import wget

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

def startingMoves():
        startingMoves = []
        #Pokemon Type Finder
        response_API = requests.get(POKEAPI_BASE_URL + "pokemon/" + pokemon)
        pokemon_info = response_API.text
        #Might put it in a list, acts like a list.
        parse_json = json.loads(pokemon_info)
        querey = parse_json["moves"]
        for move in querey:
                startingMoves.append(move["move"]["name"])
        move1 = random.choice(startingMoves)
        move2 = random.choice(startingMoves)
        move3 = random.choice(startingMoves)
        move4 = random.choice(startingMoves)
        print(move1.capitalize(), "|", move2.capitalize(), "|", move3.capitalize(), "|", move4.capitalize())
        
def pokemon_Photo_Grab():
        #Pokemon Type Finder
        response_API = requests.get(POKEAPI_BASE_URL + "pokemon/" + pokemon)
        pokemon_info = response_API.text
        #Might put it in a list, acts like a list.
        parse_json = json.loads(pokemon_info)
        querey = parse_json["sprites"]
        photo = querey["front_default"]
        return photo
        

if __name__ == '__main__':
        pokemon = input("Please Enter the Name of a Pokemon\n").lower()
        abilityPicker()
        pokemonType()
        startingMoves()
        front_photo_url = pokemon_Photo_Grab()
        photoToBeDisplayed = wget.download(front_photo_url)
        print(photoToBeDisplayed)

        root = Tk()
        root.title(pokemon)

        mainframe = ttk.Frame(root, padding = "3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text=pokemon.capitalize()).grid(column=2, row=2, sticky=(W, E))
        picture=Label(image=photoToBeDisplayed.strip())
        picture.pack()




        root.mainloop()


    
    
