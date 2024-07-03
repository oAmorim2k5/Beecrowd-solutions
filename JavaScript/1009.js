var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var name = String(lines[0]);
var salary = parseFloat(lines[1]);
var sale = parseFloat(lines[2]);

console.log(`TOTAL = R$ ${(salary+(sale*0.15)).toFixed(2)}`);