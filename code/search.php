<?php
/**
  *   Based on the search query this file will output the spotify uri.
  */
function pre($array){
    echo "<pre>";
    print_r($array);
    echo "</pre>";
}



$query = $argv[1];
$kinds = array();
foreach($kinds as $kind){
    if(substr($query, 0, 2) == $kind){
        $choice = $kind;
        $query = substr($query, 2);
    }
    else{
        $choice = 'tr';
    }
}

//echo $choice;
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

$baseLink = 'http://ws.spotify.com/search/1/';
$format = '.json';
$searchPattern = "?q=".htmlentities($query);
$searchPattern = str_replace('\ ', '%20', $searchPattern);
$link = $baseLink.$kind.$format.$searchPattern;
echo $link;
$json = file_get_contents($link);
$data = json_decode($json);
exit(0);

//$tracks = $data['track'];
//$albums = $data['album'];
//$artist = $data['artist'];


//$json = file_get_contents('http://ws.spotify.com/search/1/track.json?q=Haste%20The%20Day');
//$data = json_decode($json);
//echo $json;

pre($data);

?>