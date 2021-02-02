#!/usr/bin/node
/*
script that searches the second biggest integer in the list of arguments
*/
function secondBiggest () {
  if (process.argv.length <= 3) {
    return (0);
  }
  const myArray = [];
  for (let i = 2; i < process.argv.length; i++) {
    myArray.push(process.argv[i]);
  }
  myArray.sort((a, b) => a - b);
  return myArray[myArray.length - 2];
}
console.log(secondBiggest());
