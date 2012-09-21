import urllib2, json
from pprint import pprint
import sys
class spotifyAPI:
    def __init__(self, query, location):
        self.query = query
        self.location = location
        #
        # contains all search options
        # tr => track
        # al => album
        # ar => artist
        #
        # added spaces to the key's to make sure it is a search string with
        # specified search option
        # 
        self.choises = {'tr ':'track', 'al ':'album', 'ar ':'artist'}
        #contains the complete formatted spotify api url
        self.url = ''
        #the basis of the spotify api url
        self.baseLink = 'http://ws.spotify.com/search/1/'
        #the format of the api result
        self._format = '.json'
        #contains the choise
        self.choise = ''
        #the json result
        self.jsonObject = {}
        #array of the search result
        self.result = {}
        
        for value in self.choises:
            choise = self.query[0:3]
            if choise == value:
                self.choise = self.choises[value]
                self.query = self.query[3:]
        self.makeUrl()
    
    def makeUrl(self):
        searchPattern = "?q="+self.query.replace(' ', '+')
        self.url = self.baseLink+self.choise+self._format+searchPattern
    
    def fetchUrl(self):
        #print self.url
        try:
            urllib2.urlopen(self.url)
            response = urllib2.urlopen(self.url)
            jsonString = response.read()
            self.jsonObject = json.loads(jsonString)
        except urllib2.HTTPError, err:
                if err.code == 503:
                    print "API unavailble"
                    print self.url
                    sys.exit(0)
                elif err.code == 400:
                    print "Bad Request"
                    sys.exit(0)
                elif err.code == 403:
                    print "Rate limit reached"
                    sys.exit(0)
                elif err.code == 404:
                    print "not found"
                    sys.exit(0)
                elif err.code == 406:
                    print 'format not accepteble'
                    sys.exit(0)
                elif err.code == 500:
                    print 'internal server error'
                    sys.exit(0)
        return self
    
    
    def parseJson(self):
            if self.choise == 'track':
                #print 'track!'
                self.parseTrack()
            elif self.choise == 'album':
                #print 'album!'
                self.parseAlbum()
            elif self.choise == 'artist':
                #print 'artist'
                self.parseArtist()
            return self
    
    def parseTrack(self):
        #parse the tracks!
        queryInfo = self.jsonObject['info']
        i = 0
        tracks = []
        for track in self.jsonObject['tracks']:
            tracks.append({'name':track['name'], 'href':track['href']})
        self.result = tracks
        
    def parseAlbum(self):
        queryInfo = self.jsonObject['info']
        albums = []
        for album in self.jsonObject['albums']:
            if self.checkAvailability(album['availability']):
                pprint(album['availability'])
                albums.append({'name':album['name'], 'href':album['href']})
        self.result = albums
        
    def parseArtist(self):
        queryInfo = self.jsonObject['info']
        #parse the artists
        artists = []
        for artist in self.jsonObject['artists']:
            pprint(artist)
            #artists.append({'name':artist['name'], 'href':artist['href']})
        self.result = artists
    
    def checkAvailability(self, locations):
        if self.location in locations['territories']:
            return True
        else:
            return False