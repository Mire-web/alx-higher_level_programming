#!/usr/bin/node
11;rgb:0000/0000/0000module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 ) {
      this.width = w;
      this.height = h;
    }
  }
};
