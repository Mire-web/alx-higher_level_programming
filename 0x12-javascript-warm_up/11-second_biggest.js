#!/usr/bin/node
const { argv } = require('node:process');
let maxi = 0;
let secondMaxi = 0;
if (argv.length === 3) {
  console.log(0);
} else if (argv.length > 3) {
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] > maxi) {
      secondMaxi = maxi;
      maxi = argv[i];
    }
  }
  console.log(secondMaxi);
} else {
  console.log(0);
}
