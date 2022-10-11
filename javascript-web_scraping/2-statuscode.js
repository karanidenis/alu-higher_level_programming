#!/usr/bin/node
const url = process.argv;
const request = require('request');

request(url, (error, response, bosy)=> {
  if (error) throw (error);
  else {
    console.log(`code: ${response.statusCode}`)
  }
});
