#!/usr/bin/node

exports.esrever = function (list) {
  const reverse = [];
  let i = list.length - 1;
  for (i; i >= 0; i--) {
    reverse.push(list[i]);
  }
  return reverse;
};

// const esrever = require('./8-esrever').esrever;

// console.log(esrever([1, 2, 3, 4, 5]));
// console.log(esrever(["School", 89, { id: 12 }, "String"]));
