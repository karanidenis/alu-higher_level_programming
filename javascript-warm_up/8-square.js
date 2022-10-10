#!/usr/bin/node
let square = '';
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    square = '';
    for (let y = 0; y < args[2]; y++) {
      square += 'X';
    }
    console.log(square);
  }
}
