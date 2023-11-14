#!/usr/bin/node

const myVar = Number(process.argv[2]);
function factorial (a) {
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}

if (myVar) {
  console.log(factorial(myVar));
} else {
  console.log(1);
}
