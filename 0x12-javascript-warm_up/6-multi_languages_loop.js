#!/usr/bin/node
/*
script that prints 3 lines using an array and a loop
*/
const arrayStrings = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (let i = 0; i < arrayStrings.length; i++) {
  console.log(arrayStrings[i]);
}
/*
Another way:
arrayStrings.forEach(function (element, array) {
  console.log(element);
}); */
