#!/usr/bin/node
if (args.length === 1) {
    console.log('Argument found');
  } else if (args.length > 3) {
    console.log('Arguments found');
  } else {
    console.log('No argument');
  }