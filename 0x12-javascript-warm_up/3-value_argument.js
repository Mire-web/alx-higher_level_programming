#!/usr/bin/node

const { argv } = require('node:process');

let myVar = argv[2];

if (myVar) {
  console.log(myVar);
} else {
  console.log('No argument');
}
