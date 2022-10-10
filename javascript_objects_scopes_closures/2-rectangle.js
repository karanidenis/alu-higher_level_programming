#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w === 0 || h === 0) return null;
    if (w <= 0 || h <= 0) return null;
    this.width = w;
    this.height = h;
  }
};
