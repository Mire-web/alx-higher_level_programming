#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let i = list.length;
  while (i > 0) {
    newList.push(list.pop());
    i--;
  }
  return newList;
};
