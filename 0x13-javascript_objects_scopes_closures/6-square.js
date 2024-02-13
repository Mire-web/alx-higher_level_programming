#!/usr/bin/node
const ParentSquare = require('./5-square');

module.exports = class Square extends ParentSquare {
  charPrint (c) {
    if (c) {
      let h = this.height;
      while (h > 0) {
        let w = this.width;
        let line = '';
        while (w > 0) {
          line += c;
          w--;
        }
        console.log(line);
        h--;
      }
    } else {
      this.print();
    }
  }
};
