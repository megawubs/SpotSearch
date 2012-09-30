from code import spotifyAPI, optionlist
import sys, locale
from pprint import pprint

#get users location
locatie = locale.getdefaultlocale()
#only the capital country code is needed
locatie = locatie[0][3:]
#initize spotify api
spot = spotifyAPI(sys.argv[1], locatie)
#print the result
#pprint(spot.fetchUrl().fetchUrl())
spot.fetchUrl().parseJson()
gui = optionlist(spot.result)
gui.makeList()
#pprint(spot.result)

