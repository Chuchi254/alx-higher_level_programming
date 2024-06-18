#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

const firstInt = parseInt(args[0]);
const secondInt = parseInt(args[1]);

if (isNaN(firstInt) || isNaN(secondInt)) {
  console.log('NaN');
} else {
  console.log(add(firstInt, secondInt));
}
