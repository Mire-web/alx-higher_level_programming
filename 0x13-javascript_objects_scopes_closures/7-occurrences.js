exports.nbOccurences = function (list, searchElement) {
  let result = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      result++;
    }
    i++;
  }
  return result;
};
