#!/usr/bin/node
const args = process.argv;
if (args.length === 1) {
  console.log('Argument found');
} else if (args.length > 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
