#!/usr/bin/node
const args = process.argv.slice(1);
let count = 0;

while (args[count] !== undefined) {
  count++;
}

if (count === 0) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
