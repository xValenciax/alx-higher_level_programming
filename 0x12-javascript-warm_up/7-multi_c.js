#!/usr/bin/node

const args = process.argv.slice(2);

if (!parseInt(args[0]))
    console.log('Missing number of occurrences');

for (var i = 0; i < parseInt(args[0]); i++) {
    console.log('C is fun');
}