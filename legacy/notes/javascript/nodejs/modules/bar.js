const square = require('./square.js');
var mySquare = square(2);

// ES6에서 `로 console.log 찍으면 이렇게 변수를 + 없이 쓸 수 있음
console.log(`The area of my square is ${mySquare.area()}`);
