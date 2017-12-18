const name = "Andrew";

const sayName = () => {
  const message = "My name is " + name;
  console.log(message);
}

/*
function sayName() {
  const message = "My name is " + name;
  console.log(message);
}
*/


const sayBye = () => {
  console.log("Bye " + name);  
}

// Concise:
const sayBye = () => console.log("Bye" + name);

/*
function sayBye() {
console.log("Bye " + name);  
}
*/