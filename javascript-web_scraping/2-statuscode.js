#!/usr/bin/node
const url = process.argv;
const request = require('request');

request(url, (err, response, bosy)=> {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`)
  }
});
