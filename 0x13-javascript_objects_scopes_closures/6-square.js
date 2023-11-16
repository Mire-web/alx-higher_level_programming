const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c = 'X') {
    let w = this.width;
    let h = this.height;
    let result = '';
    while (h > 0) {
      while (w > 0) {
        result += c;
        w--;
      }
      console.log(result);
      h--;
    }
  }
};
