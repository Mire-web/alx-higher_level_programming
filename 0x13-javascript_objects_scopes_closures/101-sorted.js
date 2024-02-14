#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
Object.getOwnPropertyNames(dict).forEach(key => {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
});
console.log(newDict);
