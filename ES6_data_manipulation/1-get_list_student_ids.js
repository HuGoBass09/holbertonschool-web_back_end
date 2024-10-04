function getListStudentIds(arr) {
  if (!arr || !Array.isArray(arr)) {
    return [];
  }

  return arr.map((item) => item.id);
}

export default getListStudentIds;
