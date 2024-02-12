#!/usr/bin/node
const newArr = process.argv.slice(2,);
if (process.argv.length < 3 || newArr.length === 1) {
  console.log(0);
} else {
  newArr.sort((a,b)=> b - a)
  console.log(newArr[1]);
}
