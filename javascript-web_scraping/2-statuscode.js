#!/usr/bin/node
const url = process.argv;
const request = require('request');

request(url, (err, response, bosy)=> {
  if (err) throw (err);
  else {
    console.log(`code: ${response.statusCode}`)
  }
});
