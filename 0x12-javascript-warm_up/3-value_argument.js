#!/usr/bin/node
/*
script that prints the first argument passed to in
*/
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
