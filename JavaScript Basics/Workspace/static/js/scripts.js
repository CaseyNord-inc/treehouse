function getRandomNumber(lower, upper) {
    if (isNaN(lower) || isNaN(upper)) {
        throw new Error('Both arguments must be integers.')
    }
    return Math.floor(Math.random() * (upper - lower +1)) + lower;    
}
console.log(getRandomNumber(10, "onehundred"));

function getArea(width, length, unit) {
    var area = width * length;
    return area + " " + unit;
}
//console.log(getArea(12, 24, 'sq ft'))

