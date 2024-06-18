#!/usr/bin/node
const args = process.argv.slice(2);
const size = parseInt(args[0]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const line = 'X'.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(line);
  }
}
