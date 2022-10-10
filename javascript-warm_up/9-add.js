#!/usr/bin/node
const args = process.argv;
function add(a, b) {
    a = Number(args[2]);
    b = Number(args[3]);
    let sum = a + b;
    console.log(sum);
}
