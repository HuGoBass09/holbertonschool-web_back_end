function getStudentsByLocation(students, city) {
  if (!students || !Array.isArray(students)) {
    return [];
  }

  return students.filter((element) => (element.location === city));
}

export default getStudentsByLocation;
