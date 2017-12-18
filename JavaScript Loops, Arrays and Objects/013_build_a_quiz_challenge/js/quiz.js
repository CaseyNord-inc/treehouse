var questions = [
  ['How many minutes does it take to bake the perfect butterflied chicken breast?', '22'],
  ['How many licks does it take to get to the center of a Tootsie Pop?', '252'],
  ['What is the sum of the letters in TACOCAT?', '63'],
  ['How many pounds of wood COULD a woodchuck chuck if a woodchuck could chuck wood?', '700'],
  ['When did the war of 1812 take place?', '1812'],
];
var numberCorrect = 0;
var correctAnswers = [];
var wrongAnswers = [];
var html;

function print(message) {
  var outputDiv = document.getElementById('output');
  outputDiv.innerHTML = message;
}

function buildList(arr) {
  var listHTML = '<ol>';
  for (var i = 0; i < arr.length; i++) {
    listHTML += '<li>' + arr[i] + '</li>';
  }
  listHTML += '</ol>';
  return listHTML;
}

for (var i = 0; i < questions.length; i++) {
  var answer = prompt(questions[i][0]);
  if (answer === questions[i][1]) {
    numberCorrect++;
    correctAnswers.push(questions[i][0]);
  } else {
    wrongAnswers.push(questions[i][0]);
  }
}

if (numberCorrect ===  questions.length) {
  html = "<p>Congratulations, you got every question correct! You are a quiz master!</p>";
} else if (numberCorrect === 0) {
  html = "<p>Too bad, you didn't get any questions correct. Try harder next time!</p>";
} else {
  html = "<p>Good try! You got " + numberCorrect + " questions correct!</p>";
  html += "<h2>You got these questions correct!</h2>";
  html += buildList(correctAnswers);
  html += "<h2>You got these questions wrong...</h2>";
  html += buildList(wrongAnswers);
}

print(html);
