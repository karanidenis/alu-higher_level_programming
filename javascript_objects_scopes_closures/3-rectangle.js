#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w == null || h == null) return null;
    if (w <= 0 || h <= 0) return null;
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
  
//   const Rectangle = require('./3-rectangle');

//   const r1 = new Rectangle(2, 3);
//   r1.print();
//   const r2 = new Rectangle(10, 5);
//   r2.print();