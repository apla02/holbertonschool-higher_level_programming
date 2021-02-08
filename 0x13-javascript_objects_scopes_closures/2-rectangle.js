#!/usr/bin/node
/*
an class Rectangle that defines a rectangle
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      Object.create(Rectangle);
    } else if (w && h) {
      this.width = w;
      this.height = h;
    }
  }
};
