import requests
POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

if __name__ == '__main__':
    ditto_info = requests.get(POKEAPI_BASE_URL + "pokemon/ditto").json()
    print(ditto_info)
