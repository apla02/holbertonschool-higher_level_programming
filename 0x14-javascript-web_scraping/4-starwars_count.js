#!/usr/bin/node
const request = require('request');
const url = process.argv[2]; // url of API

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const resultList = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < resultList.length; i++) {
      for (let j = 0; j < resultList[i].characters.length; j++) {
        if (resultList[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
