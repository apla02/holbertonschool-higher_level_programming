#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const myDict = {};

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonDict = JSON.parse(body);
    for (const task of jsonDict) {
      if (task.completed === true) {
        if (myDict[task.userId] === undefined) {
          myDict[task.userId] = 1;
        } else {
          myDict[task.userId] += 1;
        }
      }
    }
    console.log(myDict);
  }
});
