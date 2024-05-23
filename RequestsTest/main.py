import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_post = {
    "name": "generate",
    "photo": "generate"
}

body_put = {
    "pokemon_id": "26501",
    "name": "generate",
    "photo": "generate"
}

body_pokeball = {
    "pokemon_id": "26500"
}

response_post = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_post)
print(response_post.text)

response_put = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_put.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
