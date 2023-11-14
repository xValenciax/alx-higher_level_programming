#!/usr/bin/node
const args = process.argv.slice(2);

const size = parseInt(args[0]);

if (!size) { console.log('Missing size'); }

const square = [];

for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    square.push('x');
  }
  square.push('\n');
}

square.pop();
console.log(square.join(''));
