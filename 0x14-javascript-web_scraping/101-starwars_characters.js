#!/usr/bin/node
/*
Script to return all characters in a starwars movie in the order it appeared
AUTHOR: MIRE-WEB
*/
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, res, body) => {
    if (err) throw err;
    else {
      const characters = JSON.parse(body).characters;
      (async () => {
        try {
          for (const character of characters) {
            const name = await new Promise((resolve, reject) => {
              request(character, (err, res, body) => {
                if (err) reject(err);
                else {
                  resolve(JSON.parse(body).name);
                }
              });
            });
            console.log(name);
          }
        } catch (err) {
          console.error(err);
        }
      })();
    }
  });
