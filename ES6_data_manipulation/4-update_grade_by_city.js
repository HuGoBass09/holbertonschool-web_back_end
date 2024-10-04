function updateStudentGradeByCity(listOfStudents, city, newGrade) {
  listOfStudents.filter((student) => (student.location === city))
    .map((item) => {
      const newRecord = { ...item };
      const newStudent = newGrade.find((student) => student.studentId === item.id);
      if (newStudent) newRecord.grade = newStudent.grade;
      else newRecord.grade = 'N/A';
      return newRecord;
    });
}

export default updateStudentGradeByCity;
