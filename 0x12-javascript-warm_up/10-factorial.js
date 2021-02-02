#!/usr/bin/node
/*
prints the addition of 2 integers
*/
function factorial (n) {
  if (parseInt(n) === 0) {
    return (1);
  } else if (isNaN(parseInt(n))) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(parseInt(process.argv[2])));
