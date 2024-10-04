function getStudentsByLocation(students, city) {
  students.filter((element) => (element.location === city));
}

export default getStudentsByLocation;
