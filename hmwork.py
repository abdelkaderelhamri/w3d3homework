# This class should have a list attribute that holds pokemon moves which should be populated with an api call to the PokeApi moves section. 
# Finally create a class method that teaches your pokemon up to 4 moves.

import requests

class Move_Tutor(Pokemon):
    def __init__(self):
        super().__init__()
        self.move_list = self.get_moves()
    
    def get_moves(self):
        response = requests.get('https://pokeapi.co/api/v2/move/')
        data = response.json()
        move_list = [move['name'] for move in data['results']]
        return move_list
    
    @classmethod
    def teach_moves(cls, pokemon, moves):
        if len(moves) > 4:
            raise ValueError('A Pokemon can only learn up to 4 moves.')
        for move in moves:
            if move not in cls.move_list:
                raise ValueError(f'{move} is not a valid move.')
        pokemon.moves = moves

class Pikachu(Pokemon):
    def __init__(self, name="Pikachu", level=1, moves=[]):
        super().__init__(name=name, level=level, moves=moves)
move_tutor = Move_Tutor()
moves_to_teach = ['Thunderbolt', 'Quick Attack', 'Iron Tail', 'Thunder Wave']
Move_Tutor.teach_moves(pikachu, moves_to_teach)
pikachu = Pikachu(name="Pikachu", level=10, moves=["Thunder Shock", "Quick Attack"])


    