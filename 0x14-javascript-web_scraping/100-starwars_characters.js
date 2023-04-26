#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  const characterRequests = characters.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  });

  Promise.all(characterRequests)
    .then((characterNames) => {
      characterNames.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.log(error);
    });
});
