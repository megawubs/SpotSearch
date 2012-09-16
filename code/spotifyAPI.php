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
      */
    public $choices = array('tr','al', 'ar');
    /**
      *  the spotify api url 
      */
    private $url;
    /**
      *  basis of the spotify api url 
      */
    private $baseLink = 'http://ws.spotify.com/search/1/';
    /**
      *  the  
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
    /*
     * __construct()
     * @param $query
     */
    
    public function __construct($query) {
        foreach($this->choices as $kind){
            if(substr($query, 0, 2) == $kind){
                $choice = $kind;
                $this->query = substr($query, 2);
            }
            else{
                $choice = 'tr';
                $this->query = $query;
            }
        }
        switch($choice){
            case "tr":
                $kind = 'track';
                break;
            case "al":
                $kind = 'album';
                break;
            case 'ar':
                $kind = 'artist';
                break;
        }
        $this->choice = $kind;
        $this->make_url();
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
        $searchPattern = str_replace('\ ', '%20', $searchPattern);
        $this->url = $this->baseLink.$this->kind.$this->format.$searchPattern;
    }
}

?>