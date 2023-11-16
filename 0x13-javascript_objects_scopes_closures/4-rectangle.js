module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let result = '';
    let w = this.width;
    let h = this.height;
    while (h > 0) {
      while (w > 0) {
        result += 'X';
        w--;
      }
      console.log(result);
      h--;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
