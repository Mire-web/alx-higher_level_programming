#!/usr/bin/node

if (Number(process.argv[2])) {
  let i;
  let j;
  let sq = '';
  for (i = 0; i < Number(process.argv[2]); i++) {
    for (j = 0; j < Number(process.argv[2]); j++) {
      sq += 'X';
    }
    console.log(sq);
    sq = '';
  }
} else {
  console.log('Missing size');
}
