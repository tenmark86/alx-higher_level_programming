#!/usr/bin/node
/*
* Write a script that prints the number of movies where the character “Wedge Antilles” is present.
* The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
* Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
*/

const axios = require('request');
const url = process.argv[2];
let count = 0;

axios(url, function (err, response, body) {
  if (!err) {
    const jsoon = JSON.parse(body);
    const res = jsoon.results;
    for (let i = 0; i < res.length; i++) {
      if (res[i].characters) {
        for (const line of res[i].characters) {
          if (line.includes('18')) {
            count++;
          }
        }
      }
    }
    console.log(count);
  } else {
    console.log(err);
  }
});
