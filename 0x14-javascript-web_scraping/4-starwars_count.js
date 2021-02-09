#!/usr/bin/node
const request = require('request');
const url = process.argv[2]; // url of API

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonDict = JSON.parse(body);
    let count = 0;
    for (const films of jsonDict.results) {
      for (const i of films.characters) {
        if (i === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
