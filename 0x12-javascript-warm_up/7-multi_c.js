#!/usr/bin/node

let myVar = Number(process.argv[2]);
if (myVar) {
  while (myVar > 0) {
    console.log('C is fun');
    myVar--;
  }
} else {
  console.log('Missing number of occurences');
}
