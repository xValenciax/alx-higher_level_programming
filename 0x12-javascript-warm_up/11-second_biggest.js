#!/usr/bin/node
const args = process.argv.slice(2);

if (!args) { console.log(0); } else {
  let max = args[0];
  let secMax = args[0];
  for (const arg of args) {
    if (arg > max) {
      secMax = max;
      max = arg;
    }
  }
  console.log(secMax);
}
