#!/usr/bin/node
/*
 * Write a script that prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line
 */

const axios = require('axios');
const url = ('https://swapi-api.hbtn.io/api/films/');
const film = process.argv[2];

axios.get(url + film)
  .then(function (response) {
    for (const x in response.data.characters) {
      const people = response.data.characters[x];
      axios.get(people)
        .then(function (response) {
          console.log(response.data.name);
        });
    }
  });
