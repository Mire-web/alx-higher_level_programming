#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOc = 0;
  let i = 0;
  while (list[i]) {
    list[i] === searchElement && nOc++;
    i++;
  }
  return nOc;
};
