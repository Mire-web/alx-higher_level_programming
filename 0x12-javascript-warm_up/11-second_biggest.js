#!/usr/bin/node

const arr = [];
let i;
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (i = 2; i < process.argv.length; i++) {
    arr.push(Number(process.argv[i]));
  }
  arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}
