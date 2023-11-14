#!/usr/bin/node
function factorial (n) {
  if (!n || n === 1) { return 1; }

  return n * factorial(n - 1);
}

const args = process.argv.slice(2);

console.log(factorial(parseInt(args[0])));
