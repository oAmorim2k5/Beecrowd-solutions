var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');
let pontOne = lines.shift().split(' ');
let pontTwo = lines.shift().split(' ');

let x1 = parseFloat(pontOne[0]);
let y1 = parseFloat(pontOne[1]);
let x2 = parseFloat(pontTwo[0]);
let y2 = parseFloat(pontTwo[1]);

let distance = Math.sqrt( Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));
console.log(distance.toFixed(4));