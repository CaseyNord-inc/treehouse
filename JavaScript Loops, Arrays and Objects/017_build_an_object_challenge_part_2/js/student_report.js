var message = '';
var search = [];
var student;

function print(message) {
    var outputDiv = document.getElementById('output');
    outputDiv.innerHTML = message;
  }

while (true) {
    var input = prompt("Student record search: Enter a [name] or type 'quit' to execute search");
    search.push(input)
    if (input === null || input.toLowerCase() === 'quit') {
        break;
    }
}

for (var i = 0; i < search.length; i++) {
    for (var j = 0; j < students.length; j++) {
        // Object array is referenced here.
        student = students[j];
        if (search[i] === student.Name) {
            message += '<h2>Student: ' + student.Name + '</h2>';
            for (var key in student) {
                if (key !== 'Name') {
                    message += '<p>' + key + ': ' + student[key] + '</p>';
                }
            }
        }
    }
}

print(message);