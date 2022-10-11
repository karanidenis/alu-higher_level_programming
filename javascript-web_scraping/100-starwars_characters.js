#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;
    data.forEach(charUrl => {
      request(charUrl, (err, resp, bdy) => {
          if (err) console.log(err);
            else {
              console.log(JSON.parse(bdy).name);
            }
        });
    });
  }
});
