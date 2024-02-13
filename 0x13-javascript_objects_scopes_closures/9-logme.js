#!/usr/bin/node
let NoPrintedArgument = 0;
exports.logMe = function (item) {
  console.log(NoPrintedArgument + ': ' + item);
  NoPrintedArgument++;
};
