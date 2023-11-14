#!/usr/bin/node
const { argv } = require('node:process');
let myVar = Number(argv[2]);
let row = myVar;
let result = '';
if (myVar) {
  while (myVar > 0) {
    while (row > 0) {
      result += 'X';
      row--;
    }
    console.log(result);
    myVar--;
  }
} else {
  console.log('Missing size');
}
