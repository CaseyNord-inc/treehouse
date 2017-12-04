alert("How many of these questions can you answer correctly?");

var correctAnswers = 0;

var q1 = prompt("What is 2 + 2?");
q1.toUpperCase();
if (q1 === '4' || q1 === 'four') {
    correctAnswers += 1;
}
var q2 = prompt("What is the meaning of life?");
q2.toUpperCase();
if (q2 === '42' || q2 === 'forty two' || q2 === 'forty-two') {
    correctAnswers += 1;
}
var q3 = prompt("How many licks does it take to get to the center of a Tootsie Pop");
if (q3 === '364' || q3 === '252') {
    correctAnswers += 1;
}
var q4 = prompt("What is the air speed velocity of an unladen swallow?");
if (q4 === '31' || q4 === '32' || q4 === '33' || q4 === '34' || q4 === '35' || q4 === '36' || q4 === '37' || q4 === '38' || q4 === '39' || q4 === '40') {
    correctAnswers += 1;
}
var q5 = prompt("How do blind people know when to stop wiping?");
q5.toUpperCase();
if (q5 === 'they don\'t' || q5 === 'feel' || q5 === 'magic' || q5 === 'sixth sense') {
    correctAnswers += 1;
}

if (correctAnswers === 5) {
    alert("You got every question correct, you are a genius!!");
} else if (correctAnswers > 3) {
    alert("You did pretty good, not greath, but pretty good.");
} else if (correctAnswers > 1) {
    alert("I'm only acknowleding that you got at least one correct.");
} else {
    alert("For your sake I'm just going to try to pretend that you never even tries this quiz...");
}