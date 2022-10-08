#!/usr/bin/node
const args = process.argv;
if (typeof args[2] !== Number) {
  console.log('Not a number');
} else {
  console.log(`My number: ${args[2]}`);
}
