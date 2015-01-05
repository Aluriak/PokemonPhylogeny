# -*- coding: utf-8 -*-
#########################
#       POKEMON VIEWER  #
#########################


#########################
# IMPORTS               #
#########################
import pickle
import random
from common.pokemon import Pokemon
from common.common import FILE_POKEMON



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
# CONSTRUCTOR #################################################################
# PUBLIC METHODS ##############################################################
# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################
if __name__ == '__main__':
    with open(FILE_POKEMON, "rb") as fpok:
        pokemons = pickle.load(fpok)


    for pokemon in pokemons:
        # quick printing of a Pokemon instance
        #print(pokemon) 
        # that is equivalent to:
        print(pokemon.name + ' (' + ' and '.join(pokemon.types) + '): ' + ''.join(pokemon.dna))
        # a Pokémon object know its distance to another one
        random_pokemon = random.choice(pokemons) 
        print('Hamming distance between', pokemon.name, 'and', random_pokemon.name, 'is', 
              pokemon.distTo(random_pokemon) # by default its hamming distance
             )





