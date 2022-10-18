#!/usr/bin/node
/*
 * Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
 * The first argument is the movie ID
 */

const request = require('request');
const id = process.argv[2];
request('https://swapi-api.hbtn.io/films/' + id + '/', function (error, response, body) {
  if (error == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
