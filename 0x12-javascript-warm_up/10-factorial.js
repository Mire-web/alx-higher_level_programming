#!/usr/bin/node
if (!Number(process.argv[2])) {
  console.log(1);
} else {
  console.log(factorial(process.argv[2]));
}
function factorial(a) {
  let result = 1;
  if (a <= 1) {
    return result;
  } else {
    return a * factorial(a - 1);
  }
}
