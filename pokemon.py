# -*- coding: utf-8 -*-
#########################
#       POKEMON         #
#########################


#########################
# IMPORTS               #
#########################




#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
class Pokemon(object):
    """
    A Pokemon have a name, one or two types, moves id that he can learn, and a dna, based
    on the moves he can learn.
    """

    MOVES_COUNT = 559
    TYPES = {
        #-1: None,       # no type
         1: 'Steel',
         2: 'Fighting',
         3: 'Dragon',
         4: 'Water',
         5: 'Electric',
         6: 'Fire',
         7: 'Ice',
         8: 'Bug',
         9: 'Normal',
        10: 'Grass',
        11: 'Poison',
        12: 'Psychic',
        13: 'Rock',
        14: 'Ground',
        15: 'Ghost',
        16: 'Dark',
        17: 'Flying',
    }


# CONSTRUCTOR #################################################################
    def __init__(self, name):
        self.name  = name
        self.types = set()
        self.moves = set()
        self.dna   = ['0'] * Pokemon.MOVES_COUNT


# PUBLIC METHODS ##############################################################
    def appendMove(self, move_id):
        self.moves.add(move_id)

    def appendType(self, type_id):
        assert(int(type_id) in Pokemon.TYPES)
        self.types.add(int(type_id))

    def doDNA(self):
        """generate self.dna from knowed moves"""
        self.dna = "".join(['1' if _ in self.moves else '0' for _ in range(Pokemon.MOVES_COUNT)])


# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
    def __str__(self):
        return self.name + ' (' + ' and '.join([Pokemon.TYPES[t] for t in self.types]) + '): ' + ''.join(self.dna)
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################



