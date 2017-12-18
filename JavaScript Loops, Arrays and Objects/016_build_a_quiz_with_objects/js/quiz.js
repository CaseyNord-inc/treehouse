var questions = [
  {
    question: 'How many minutes does it take to bake the perfect butterflied chicken breast?',
    answer: '22'
  },
  {
    question: 'How many licks does it take to get to the center of a Tootsie Pop?',
    answer: '252'
  },
  {
    question: 'What is the sum of the letters in TACOCAT?',
    answer: '63'
  },
  {
    question: 'How many pounds of wood COULD a woodchuck chuck if a woodchuck could chuck wood?',
    answer: '700'
  },
  {
    question: 'When did the war of 1812 take place?',
    answer: '1812'
  }
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
  var answer = prompt(questions[i].question);
  if (answer === questions[i].answer) {
    numberCorrect++;
    correctAnswers.push(questions[i].question);
  } else {
    wrongAnswers.push(questions[i].question);
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
