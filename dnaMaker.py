# -*- coding: utf-8 -*-
#########################
#       MAKEDNA         #
#########################
"""
usage: makeDNA [generation_id,…]
generation_id is an integer, > 0 and < 6
Example :
    makeDNA 1 3 5
    => get data for generation 1 3 and 5
Default :
    makeDNA 1
"""


#########################
# IMPORTS               #
#########################
import sys, re, pickle, urllib
from collections import defaultdict
from bs4 import BeautifulSoup as BS
from common import NB_MOVES, FILE_POKEMON_DNA, URL_POKEBIP_POKEDEX, URL_POKEBIP_SEARCH_POKEDEX, getHTMLOf





#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
class DNAMaker(object):
    """
    """

# CONSTRUCTOR #################################################################
    def __init__(self, generations = [1], final_only = False, dna_size = NB_MOVES):
        self.final_only = final_only
        self.generations = generations
        self.dna_size = int(dna_size)


# PUBLIC METHODS ##############################################################
    def saveDNA(self, filename):
        # Save dnas in a file
        print("Saving in " + filename + "… ", end="")
        with open(filename, "wb") as fdna:
            pickle.dump(self.dnas, fdna)
        print("OK")

    def parseDNA(self):
        self.dnas = {}
        self.__operateParsing()
        self.__doDNA()
        return self.dnas



# PRIVATE METHODS #############################################################
    def __doDNA(self):
        # For each pokemon, deduce DNA
        print("DNA computation… ", end="")
        for pokemon, knowed_moves in self.pokemons.items():
            self.dnas[pokemon] = "".join(['1' if _ in knowed_moves else '0' for _ in range(1, self.dna_size)])
        print("OK")
         

    def __operateParsing(self):
        # URL construction
        self.pokedex_pokemon_url = URL_POKEBIP_SEARCH_POKEDEX 
        if self.final_only: 
            self.pokedex_pokemon_url += '&poke_evofinale=1'
        for gen_id in generation:
            self.pokedex_pokemon_url += '&poke_gen' + gen_id + '=1'

        # Get url of each pokemon
        bs = BS(getHTMLOf(self.pokedex_pokemon_url))
        # get url of all <a> tag in html page
        self.pokemon_urls = [str(a['href']) for a in bs.find_all("a", href=True) if re.compile("pokedex_5G_fiche").match(a['href'])]

        print(len(self.pokemon_urls), " Pokemon find !")


        # Pokemon treatment
        move_url = "pokedex_5G_attaque"
        regex_move_numbr = re.compile(move_url + "[0-9]*")

        # Final data container
        self.pokemons = defaultdict(list)
        self.unknow_pokemons = [] 

        # For each url, get pokemon name and moves
        for pokemon_url in self.pokemon_urls:
            # get pokemon name
            start = pokemon_url.find('__') + len('__')
            end   = pokemon_url.find('.html', start)
            pokemon_name = pokemon_url[start:end]
            print(pokemon_name + "… ", end="")
            # get all moves pokemon can learn
            try:
                bs = BS(getHTMLOf(URL_POKEBIP_POKEDEX + pokemon_url.replace(' ', '%20')))
                for a in bs.find_all('a'):
                    href = a.get('href', "")
                    regex_result = re.findall(regex_move_numbr, href) # find tags where a move url is
                    if len(regex_result) == 1:
                        move_id = int(regex_result[0][len(move_url):]) # get only the move id
                        # add move to knowed moves for current pokemon
                        self.pokemons[pokemon_name].append(move_id) 
                print("OK")
            except urllib.error.HTTPError:
                self.unknow_pokemons.append(pokemon_url)
                print("ERROR !")
            except KeyboardInterrupt:
                print("Abort parsing !")
                break


# PREDICATS ###################################################################
    def haveUnknowPokemon(self):
        return len(self.unknow_pokemons) == 0

# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################







#########################
# FUNCTIONS             #
#########################



#########################
# MAIN                  #
#########################
if __name__ == '__main__':
    # get generation number and only_final_evolution condition
    only_final_evolution = False
    if 'f' in sys.argv:
        only_final_evolution = True
        sys.argv.remove('f')
    generation = ['1'] if len(sys.argv) < 2 else sys.argv[1:]

    
    # Generate parser + do parsing
    maker = DNAMaker(generation, only_final_evolution)
    maker.parseDNA()
    maker.saveDNA(FILE_POKEMON_DNA)

            


    # Print unknow pokemons
    if maker.haveUnknowPokemon():
        print("Unknow Pokémons :")
        print(", ".join(maker.unknow_pokemons))
    else:
        print("All asked pokemons are parsed.")


