# -*- coding: utf-8 -*-
#########################
#       COMMON          #
#########################


#########################
# IMPORTS               #
#########################
import sys





#########################
# PRE-DECLARATIONS      #
#########################
FILE_POKEMON = "data/pokemons.dat"
URL_POKEBIP_POKEDEX = "http://www.pokebip.com/pokemon/pokedex/"
URL_POKEBIP_SEARCH_POKEDEX = 'http://www.pokebip.com/pokedex/index.php?phppage=gen5/liste&poke_tri=1'





#########################
# FUNCTIONS             #
#########################
def getHTMLOf(url):
    """
    @param url a valid URL string
    @return HTML of page at given URL
    """
    import urllib
    from urllib import request
    return request.urlopen(request.Request(url)).read()




#########################
# MAIN                  #
#########################






