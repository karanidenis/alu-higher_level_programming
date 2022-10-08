#!/usr/bin/node
const txt = 'C is fun';
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  for (;txt;) {
    console.log('C is fun' * args[2]);
  }
}
