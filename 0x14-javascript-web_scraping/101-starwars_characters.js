#!/usr/bin/node
/*
 * Write a script that prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line
 */

const axios = require('axios');
const url = ('https://swapi-api.hbtn.io/api/films/');
const film = process.argv[2];

async function savemovies () {
  const responses = await axios.get(url + film);
  const urlName = responses.data.characters;
  for (let i = 0; i < urlName.length; i++) {
    const people = urlName[i];
    await axios.get(people)
      .then(function (response) {
        console.log(response.data.name);
      });
  }
}
savemovies();
