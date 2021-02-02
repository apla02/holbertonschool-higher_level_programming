#!/usr/bin/node
/*
Write a script that prints a square
*/
const mySize = process.argv[2];
if (isNaN(mySize)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= mySize; i++) {
    console.log('X'.repeat(mySize));
  }
}
