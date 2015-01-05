# -*- coding: utf-8 -*-
#########################
#       POKEMOM PARSER  #
#########################
"""
usage: PokemonParser [generation_id,…]
generation_id is an integer, > 0 and < 6
Example :
    PokemonParser 1 3 5
    => get data for generation 1 3 and 5
Default :
    PokemonParser 1
"""


#########################
# IMPORTS               #
#########################
import sys, re, pickle, urllib
from collections import defaultdict
from bs4 import BeautifulSoup as BS
from common.common import FILE_POKEMON, URL_POKEBIP_POKEDEX, URL_POKEBIP_SEARCH_POKEDEX, getHTMLOf
from common.pokemon import Pokemon





#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
class PokemonParser(object):
    """
    """

# CONSTRUCTOR #################################################################
    def __init__(self, generations = [1], final_only = False):
        self.final_only = final_only
        self.generations = generations


# PUBLIC METHODS ##############################################################
    def savePokemons(self, filename = None):
        assert(self.pokemon is not None)
        # Save dnas in a file
        if filename is None: # creat automatic name
            filename = ('pokemon_' +
                ''.join([str(_) for _ in self.generations]) + 
                'f' if self.final_only else '')
        print("Saving in " + filename + "… ", end="")
        with open(filename, "wb") as fpok:
            pickle.dump(self.pokemons, fpok)
        print("OK")


    def parsePokemons(self):
        self.pokemons = {}
        self.__operateParsing()
        self.__doPokemon()
        return self.dnas



# PRIVATE METHODS #############################################################
    def __doPokemon(self):
        # For each pokemon, deduce Pokemon
        print("Pokemon computation… ", end="")
        for pokemon in self.pokemons:
            pokemon.doPokemon() 
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

        # Pokebip specific detecters
        move_url = r"pokedex_5G_attaque"
        type_url = r"images\/gen5_types\/"
        regex_move_numbr = re.compile(move_url + r"[0-9]*")
        regex_types      = re.compile(type_url + r"([0-9]{1,2})\.png") 

        # Final data container
        self.pokemons = []#defaultdict(list)
        self.unknow_pokemons = [] 

        # For each url, get pokemon name and moves
        for pokemon_url in self.pokemon_urls:
            # get pokemon name
            start = pokemon_url.find('__') + len('__')
            end   = pokemon_url.find('.html', start)
            pokemon_name = pokemon_url[start:end]
            print(pokemon_name + "… ", end="")
            pokemon = Pokemon(pokemon_name)
            # get data about this pokémon
            try:
                bs = BS(getHTMLOf(URL_POKEBIP_POKEDEX + pokemon_url.replace(' ', '%20')))
                # get the moves that can be learn
                for a in bs.find_all('a'):
                    href = a.get('href', "")
                    regex_result = re.findall(regex_move_numbr, href) # find tags where a move url is
                    if len(regex_result) == 1:
                        move_id = int(regex_result[0][len(move_url):]) # get only the move id
                        # add move to knowed moves for current pokemon
                        pokemon.appendMove(move_id) 
                # get the types: the second <tr> contain many unwanted <img>, but the regex can filter them
                for img in bs.table.find_all('tr')[1].find_all('img'):
                    #print(img.get('src', ''))
                    regex_result = regex_types.match(img.get('src', ''))
                    if regex_result is not None:
                        #print('RESULT', regex_result.group(1), 'RESULT')
                        pokemon.appendType(regex_result.group(1))
                # the end
                self.pokemons.append(pokemon)
                print("OK")
            except urllib.error.HTTPError:
                self.unknow_pokemons.append(pokemon_url)
                print("ERROR !")
            except KeyboardInterrupt:
                print("Abort parsing !")
                break


# PREDICATS ###################################################################
    def haveUnknowPokemon(self):
        return len(self.unknow_pokemons) > 0

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
    parser = PokemonParser(generation, only_final_evolution)
    parser.parsePokemons()
    parser.savePokemon(FILE_POKEMON)

            


    # Print unknow pokemons
    if parser.haveUnknowPokemon():
        print("Unknow Pokémons :")
        print(", ".join(parser.unknow_pokemons))
    else:
        print("All asked pokemons are parsed.")


