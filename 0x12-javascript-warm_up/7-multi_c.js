#!/usr/bin/node
if (!Number(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  let i = process.argv[2];
  while (i >= 1) {
    console.log('C is fun');
    i--;
  }
}
