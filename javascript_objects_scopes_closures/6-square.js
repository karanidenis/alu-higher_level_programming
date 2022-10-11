#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (C) {
    if (!C) {
    this.Print();
  } else {
      for (i = 0; i < this.height; i++) {
        console.log(C.repeat(this.width));
      }
    }
  }
};

// const s1 = new Square(4);
// s1.charPrint();

// s1.charPrint('C');
