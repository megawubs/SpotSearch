from code import spotifyAPI
import sys

spot = spotifyAPI(sys.argv[1])
spot.fetchUrl()
#print spot.jsonObject
#print spot.choises