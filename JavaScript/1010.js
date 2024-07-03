var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var lines1 = lines.shift().split(' ');
let aCode = parseInt(lines1[0]);
let aQuantity = parseInt(lines1[1]);
let aPrice = parseFloat(lines1[2]);
let atotal = aQuantity*aPrice

var lines2 = lines.shift().split(' ');
let bCode = parseInt(lines2[0]);
let bQuantity = parseInt(lines2[1]);
let bPrice = parseFloat(lines2[2]);
let btotal = bQuantity*bPrice;

console.log(`VALOR A PAGAR: R$ ${(atotal+btotal).toFixed(2)}`);