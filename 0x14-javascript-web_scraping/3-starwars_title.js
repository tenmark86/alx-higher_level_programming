#!/usr/bin/node
/*
 * Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
 * The first argument is the movie ID
 */

const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/films/' + (process.argv[2]);

axios.get(url)
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (err) {
    console.log(err.response.status);
  });
