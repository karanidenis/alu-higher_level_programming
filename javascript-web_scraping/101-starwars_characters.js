#!/usr/bin/node
const request = require('request');

const Url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

function printCharacterName (characters, index) {
  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const name = JSON.parse(body).name;
      console.log(name);
      if (index < characters.length - 1) {
        printCharacterName(characters, index + 1);
      }
    }
  });
}

request(Url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacterName(characters, 0);
  }
});
