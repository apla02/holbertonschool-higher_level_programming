#!/usr/bin/node
/*
function that counts the number of occurences in an a list
*/
exports.nbOccurences = function (list, searchElement) {
  let repetidos = 0;
  for (const value of list) {
    if (value === searchElement) {
      repetidos++;
    }
  }
  return (repetidos);
};
