const js = require('fs');

function countStudents(path) {
  let content;
  try {
    content = js.readFileSync(path, 'utf-8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = content.trim().split('\n');

  if (lines.length <= 1) {
    console.log('Number of students: 0');
    return;
  }

  const [, ...rows] = lines;
  const students = rows.map((row) => row.split(','));
  const numberOfStudents = students.length;
  console.log(`Number of students: ${numberOfStudents}`);

  const fields = {};
  for (const student of students) {
    const [name, , field] = student;
    if (!fields[field]) fields[field] = [];
    fields[field].push(name);
  }

  for (const [field, names] of Object.entries.fields) {
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  }
}

module.exports = countStudents;
