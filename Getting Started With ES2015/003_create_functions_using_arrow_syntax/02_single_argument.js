const square = (x) => {return x * x;}

// This can be made even more concise with the following:

const square = x => x * x;

// Note that you can only remove () when you have exactly 1 argument and can 
// only remove {} and the return keyword when you have just one line of code.

/*
function square(x) {
    return x * x;
}
*/

const cube = (x) => {return square(x) * x;}

/*
function cube(x) {
    return square(x) * x;
}
*/