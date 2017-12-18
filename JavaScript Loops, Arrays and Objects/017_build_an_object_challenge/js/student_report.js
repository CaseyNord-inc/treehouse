var message = '';
var student;

function print(message) {
    var outputDiv = document.getElementById('output');
    outputDiv.innerHTML = message;
  }

for (var i = 0; i < students.length; i++) {
    // Object array is referenced here.
    student = students[i];
    message += '<h2>Student: ' + student.Name + '</h2>';
    for (var key in student) {
        if (key !== 'Name') {
            message += '<p>' + key + ': ' + student[key] + '</p>';
        }
    }
}

print(message);