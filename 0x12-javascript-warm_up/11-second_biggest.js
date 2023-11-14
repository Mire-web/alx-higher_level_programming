#!/usr/bin/node

let maxi = 0;
let secondMaxi = 0;
if (process.argv.length === 3) {
  console.log(0);
} else if (process.argv.length > 3) {
  for (let i = 0; i < process.argv.length; i++) {
    if (process.argv[i] > maxi) {
      secondMaxi = maxi;
      maxi = process.argv[i];
    }
  }
  console.log(secondMaxi);
} else {
  console.log(0);
}
