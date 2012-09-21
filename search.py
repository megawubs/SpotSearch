from code import spotifyAPI
import sys, locale
from pprint import pprint

#get users location
locatie = locale.getdefaultlocale()
#only the capital country code is needed
locatie = locatie[0][3:]
#initize spotify api
spot = spotifyAPI(sys.argv[1], locatie)
#print the result
pprint(spot.fetchUrl().parseJson().result)

