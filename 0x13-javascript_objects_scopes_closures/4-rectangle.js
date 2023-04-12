#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 1 && h > 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let mm = '';
      for (let j = 0; j < this.width; j++) {
        mm += 'X';
      }
      console.log(mm);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
