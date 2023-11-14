#!/usr/bin/node

if (process.argv.length === 3) {
  console.log(0);
} else if (process.argv.length > 3) {
  const args = process.argv.map(Number).slice(2, process.argv.length).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
} else {
  console.log(0);
}
