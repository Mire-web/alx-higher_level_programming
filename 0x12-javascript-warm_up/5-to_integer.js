#!/usr/bin/node
const myVar = process.argv[2];
if (!Number(myVar)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myVar);
}
