const js = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    const content = js.readFile(path, 'utf-8', (err) => {
      if (err) {
        reject(Error('Cannot load the database'));
      }
    });

    const response = [];
    let msg;

    const lines = content.split('\n');

    if (lines.length <= 1) {
      msg = 'Number of students: 0';
      console.log(msg);
      response.push(msg);
      resolve(response);
      return;
    }

    const [, ...rows] = lines;
    const students = rows.map((row) => row.split(','));
    const numberOfStudents = students.length;
    msg = `Number of students: ${numberOfStudents}`;
    console.log(msg);
    response.push(msg);

    const fields = {};
    for (const student of students) {
      const [name, , field] = student;
      if (!fields[field]) fields[field] = [];
      fields[field].push(name);
    }

    for (const [field, names] of Object.entries(fields)) {
      msg = `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
      console.log(msg);
      response.push(msg);
    }

    resolve(response);
  });
}

module.exports = countStudents;
