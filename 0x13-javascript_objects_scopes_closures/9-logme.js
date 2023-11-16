let count = 0;

exports.logMe = function (item) {
  const text = count + ': ' + item;
  console.log(text);
  count++;
};
