#!/usr/bin/node
let argValue1 = process.argv[2] !== undefined ? process.argv[2] : "undefined";
let argValue2 = process.argv[3] !== undefined ? process.argv[3] : "undefined";
console.log(argValue1 + " is " + argValue2);