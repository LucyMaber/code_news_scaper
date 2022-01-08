import aiohttp
import asyncio


async def getPokemon():
    async with aiohttp.ClientSession() as session:
        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                return pokemon['name']

async def main():
    a = await  getPokemon()
    print(a)
    print("done")

print(asyncio.run(main()))