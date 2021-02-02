#!/usr/bin/node
/*
Write a script that prints x times “C is fun”
x is the first argument
*/
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= x; i++) {
    console.log('C is fun');
  }
}
