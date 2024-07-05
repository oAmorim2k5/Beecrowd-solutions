var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split(' ');

let A = parseInt(lines[0]);
let B = parseInt(lines[1]);
let C = parseInt(lines[2]);

let testAB = (A+B+Math.abs(A-B))/2;
let maiorABC = (C+testAB+Math.abs(C-testAB))/2;

console.log(`${maiorABC} eh o maior`);