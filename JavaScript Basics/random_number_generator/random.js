var num1 = prompt("Enter a starting number");
var bottomNumber = parseInt(num1);
var num2 = prompt("Enter another number");
var topNumber = parseInt(num2);
var randNum = Math.floor(Math.random() * (topNumber - bottomNumber + 1)) + bottomNumber;
var message = "<p>" + randNum + " is a number between " + bottomNumber + " and " + topNumber + "</p>";
document.write(message);
