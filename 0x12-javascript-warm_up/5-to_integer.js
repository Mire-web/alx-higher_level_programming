#!/usr/bin/node
const { argv } = require('node:process');

const myVar = 'My number: ' + Number(argv[2]);

if (Number(argv[2])) {
  console.log(myVar);
} else {
  console.log('Not a number');
}
