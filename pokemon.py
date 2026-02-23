import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

if __name__ == '__main__':
    pokemon_name = input("Please enter a pokemon name: ")
    pokemon_info = get_pokemon(pokemon_name.lower())
    if pokemon_info:
        print(f"Name: {pokemon_info["name"]}")
        print(f"ID: {pokemon_info["id"]}")
        print(f"Abilities: {pokemon_info["abilities"]}")