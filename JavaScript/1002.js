var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const pi = 3.14159;

let R = parseFloat(lines[0]);
let Area = pi*Math.pow(R, 2);
console.log(`A=${Area.toFixed(4)}`);