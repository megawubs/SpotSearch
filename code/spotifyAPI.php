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
    public $kinds = array('tr','al', 'ar');
    /**
      *  the spotify api url 
      */
    private $url;
    /**
      *  basis of the spotify api url 
      */
    private $baseLink = 'http://ws.spotify.com/search/1/';
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
        foreach($this->kinds as $kind){
            if(substr($query, 0, 2) == $kind){
                $this->choice = $kind;
                $this->query = substr($query, 2);
            }
            else{
                $this->choice = 'tr';
                $this->query = $query;
            }
        }
        switch($this->choice){
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
    }
}

?>