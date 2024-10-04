function hasValuesFromArray(set, arr) {
  arr.every((element) => (set.has(element)));
}

export default hasValuesFromArray;
