import asyncio
from random import randint
from time import perf_counter
from req_http import http_get_sync, http_get_async

# The highest pokemon ID
MAX_POKEMON = 898

# The HTTP request is sync, i.e. no threading
def get_random_pokemon_name_sync() -> str:
    time_before = perf_counter()
    for _ in range(20):
        pokemon_id = randint(1, MAX_POKEMON)
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        pokemon = http_get_sync(pokemon_url)
        print(str(pokemon['name']))
    print(f"Time Taken = {perf_counter() - time_before}")

# This function and the  HTTP request are async
async def get_random_pokemon_name_async() -> str:
        pokemon_id = randint(1, MAX_POKEMON)
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        pokemon = await http_get_async(pokemon_url)
        return str(pokemon['name'])

# async = this is a coroutine
# await = the method blocks so go do something else in the meanwhile. 
async def main_async() -> None:
    time_before = perf_counter()
    for _ in range(20):
        pokemon_name = await get_random_pokemon_name_async()
        print(pokemon_name)
    print(f"Time Taken = {perf_counter() - time_before}")

    time_before = perf_counter()
    result = await asyncio.gather(*[get_random_pokemon_name_async() for _ in range(20)])
    print(f"Time Taken = {perf_counter() - time_before}")
    print(result)

def main_sync() -> None:
    get_random_pokemon_name_sync()

if __name__ == "__main__":
    main_sync()
    asyncio.run(main_async())