#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  const filteredArgs = args.filter(num => num !== max);
  const secondMax = Math.max(...filteredArgs);
  console.log(secondMax);
}
