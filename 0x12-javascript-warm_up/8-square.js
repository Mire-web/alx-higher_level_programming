#!/usr/bin/node
if (!Number(process.argv[2])) {
  console.log('Missing size');
} else {
  let width = process.argv[2];
  let height = process.argv[2];
  let line = '';
  while (height > 0) {
    while (width > 0) {
      line += 'X';
      width--;
    }
    width = process.argv[2];
    console.log(line);
    line = '';
    height--;
  }
}
