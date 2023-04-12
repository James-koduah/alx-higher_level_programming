#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0) this.width = w; else {this.width = undefined;}
    if (h > 0) this.height = h; else {this.width = undefined;}
  }
};
