#!/usr/bin/node
/*
function that returns the reversed version of a list
*/
exports.esrever = function (list) {
  const reversedList = [];
  while (list.length) {
    reversedList.push(list.pop()); // take the last one and put in the first position
  }
  return (reversedList);
};
