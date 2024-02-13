#!/usr/bin/node
const argsLength = process.argv.length;
console.log(argsLength === 2 ? 'No argument' : argsLength === 3 ? 'Argument found' : 'Arguments found');
