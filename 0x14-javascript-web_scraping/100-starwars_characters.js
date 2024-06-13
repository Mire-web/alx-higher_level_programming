#!/usr/bin/node
/*
Script to return all characters in a starwars movie
AUTHOR: MIRE-WEB
*/
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, res, body) => {
    if (err) throw err;
    else {
      const characters = JSON.parse(body).characters;
      for (const character of characters) {
        request(character, (err, res, body) => {
          if (err) throw err;
          else {
            console.log(JSON.parse(body).name);
          }
        });
      }
    }
  });
