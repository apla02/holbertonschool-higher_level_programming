#!/usr/bin/node
/*
a class Square inherit from class Rectangle
*/
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      Object.create(Rectangle); // return an empty object
    } else if (w && h) {
      this.width = w;
      this.height = h;
    }
  }

  print () { // print the rectangle
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () { // changes the values of width and height
    const i = this.height;
    this.height = this.width;
    this.width = i;
  }

  double () { // doubles the measures of width and height
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size); // call the super class constructor and pass in the name parameter
  }
};
