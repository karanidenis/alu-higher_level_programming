#!/usr/bin/node
const args = process.argv;
function Factorial (y) {
  if (y === 0) {
    return 1;
  } else {
    return y * Factorial(y - 1);
  }
}
const y = parseInt(args[2]);
if (isNaN(y)) {
  console.log(1);
} else {
  console.log(Factorial(y));
}
