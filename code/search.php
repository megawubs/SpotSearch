<?php
/**
  *   Based on the search query this file will output the spotify uri.
  */
include_once 'spotifyAPI.php';

$query = $argv[1];
$spotify = new spotifyAPI($query);
//exit(0);
$data = $spotify->fetchUrl()->parseJson();
//$json = file_get_contents($link);
//$data = json_decode($json);
//exit(0);

//pre($spotify->url);

?>