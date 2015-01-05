# A Pokemon Phylogeny
Generate a DNA for each pokemon, based on moves that can be learn, and use this 0/1 sequence to do alignment and phylogeny !
In pure Python, parsing of _pokebip.com_ pokedex.
used modules:
- stdlib (pickle, urllib, sys, re)
- [BeautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4)

## Makefile
do simple shortcuts to python code calls
example:
- *python3 pokemonParser.py 3 5 f* will do DNA for all final evolution pokemons of 5 and 3 generations.

## DATA Files
data files are used for save some intermediates data, like *pokemon.dat*, where list of each requested Pokemon object is stocked with pickle.



