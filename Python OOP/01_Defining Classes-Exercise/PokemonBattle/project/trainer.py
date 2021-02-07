class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return f'This pokemon is already caught'
        self.pokemon.append(pokemon)
        return f'Caught {pokemon.name} with health {pokemon.health}'

    def release_pokemon(self, pokemon_name):
        pokemons = [p for p in self.pokemon if p.name == pokemon_name]
        if not pokemons:
            return 'Pokemon is not caught'
        pokemon = pokemons[0]
        self.pokemon.remove(pokemon)
        return f'You have released {pokemon_name}'

    def trainer_data(self):
        res = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n'
        for p in self.pokemon:
            res += '- ' + p.pokemon_details() +'\n'
        return res
