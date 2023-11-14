#!/usr/bin/node

let myVar = Number(porcess.argv[2]);
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
