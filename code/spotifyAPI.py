import urllib2, json
from pprint import pprint
class spotifyAPI:
    def __init__(self, query):
        self.query = query
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
        searchPattern = "?q="+self.query.replace(' ', '%20')
        self.url = self.baseLink+self.choise+self._format+searchPattern
    
    def fetchUrl(self):
        response = urllib2.urlopen(self.url)
        jsonString = response.read()
        self.jsonObject = json.loads(jsonString)
        pprint(self.jsonObject)