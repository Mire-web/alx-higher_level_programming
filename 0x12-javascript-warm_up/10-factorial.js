#!/usr/bin/node

function factorial (a) {
  if (a > 0) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}

console.log(factorial(Number(process.argv[2])));
