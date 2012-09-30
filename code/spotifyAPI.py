import urllib2, json, sys
from pprint import pprint
from HTMLParser import HTMLParser

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
        self.spotifyOpenLink = 'http://open.spotify.com/'
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
        self.spotifyOpenLink+=self.choise+'/'
    
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
            if self.checkAvailability(track['album']['availability']):
                image = self.getImages(track['href'])
                tracks.append({'name':track['name'], 'href':track['href'], 'image':image})
        self.result = tracks
        
    def parseAlbum(self):
        queryInfo = self.jsonObject['info']
        albums = []
        for album in self.jsonObject['albums']:
            if self.checkAvailability(album['availability']):
                image = self.getImages(album['href'])
                albums.append({'name':album['name'], 'href':album['href'], 'image':image})
        self.result = albums
        
    def parseArtist(self):
        queryInfo = self.jsonObject['info']
        #parse the artists
        artists = []
        for artist in self.jsonObject['artists']:
            image = self.getImages(artist['href'])
            artists.append({'name':artist['name'], 'href':artist['href'], 'image':image})
        self.result = artists
    
    def checkAvailability(self, locations):
        if self.location in locations['territories']:
            return True
        else:
            return False
    
    def getImages(self, href):
        href = href.split(':')
        link = self.spotifyOpenLink
        link+=href[2]
        parser = OpenSpotifyParser()
        try:
            response = urllib2.urlopen(link)
            html = response.read()
            html = html.decode('utf-8')
            parser.feed(html)
            result = parser.image
        except urllib2.HTTPError:
            print "no connection to spotify"
            exit(1)
        return result
        
            
class OpenSpotifyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            if attrs[0][1] == "cover-art":
                self.image = attrs[1][1]
        return self