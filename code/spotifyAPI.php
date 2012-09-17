<?php

/*
 * class spotifyAPI
 */

class spotifyAPI {
    /**
      *  contains all search options
      *  tr => track
      *  al => album
      *  ar => artist
      *
      *  added spaces to the key's to make sure it is a search string with
      *  specified search option
      */
    public $choices = array('tr '=>'track','al '=>'album', 'ar '=>'artist');
    /**
      *  the spotify api url 
      */
    private $url;
    /**
      *  basis of the spotify api url 
      */
    private $baseLink = 'http://ws.spotify.com/search/1/';
    /**
      *  the varible that contains the format we want out data to recieve in
      */
    private $format = '.json';
    /**
      *  the search query 
      */
    private $query;
    /**
      *  contains the choice 
      */
    private $choice;
    /**
      *  the json object 
      */    
    private $json;
    /**
      *  array of the search result 
      */
    public $result;
    /*
     * __construct()
     * @param $query
     */
    
    public function __construct($query) {
        //echo $query;
        $choice = '';
        foreach($this->choices as $key=>$kind){
            if(substr($query, 0, 3) == $key){
                $choice = $this->choices[$key];
                $this->query = substr($query, 3);
            }
        }
        if(empty($choice)){
            $choice = $this->choices['tr '];
        }
        $this->choice = $choice;
        $this->make_url();
        //echo $this->choice;
    }
    
    /*
     * creates the url
     *
     * function make_url
     * @param 
     * @throws 
     * @return 
     */
    
    private function make_url() {
        $searchPattern = "?q=".htmlentities($this->query);
        $searchPattern = str_replace(' ', '%20', $searchPattern);
        $this->url = $this->baseLink.$this->choice.$this->format.$searchPattern;
    }
    
    /*
     * fetches $this->url and makes an object of the json return
     * stores it in $this->json
     *
     * function fetchUrl
     * @return this
     */
    
    public function fetchUrl() {
        $json = file_get_contents($this->url);
        $this->json = json_decode($json);
        return $this;
    }
    /**
      *  parses the json object
      *
      *  @return this
      */
    public function parseJson(){
        print_r($this->json);
        if($this->choice == 'track'){
            //we're dealing with a lot of data!
            $result = $this->parseTracks();
        }
        elseif($this->choice == 'album'){
            //also a lot of data!
           $result = $this->parseAlbums();
        }
        elseif($this->choice == 'artist'){
            //easy data!
            $result = $this->parseArtist();
        }
        $this->result = $result;
    }
    
    /*
     * parses the result from a track search
     *
     * function parseTracks
     * @param 
     * @throws 
     * @return array
     */
    
    private function parseTracks() {
        //parse all tracks and return an array with name and spotify uri
    }
    
    /*
     * parses the result fomr a album search
     *
     * function parseAlbum
     * @param 
     * @throws 
     * @return Array
     */
    
    private function parseAlbum() {
        //parse all albums an return an array with name and spotify uri
    }
    
    /*
     * pases an artist search
     *
     * function parseArtist
     * @param 
     * @throws 
     * @return Array
     */
    
    private function parseArtist() {
        //parse the artist result and return an array with name and spotify uri
    }
    
}

?>