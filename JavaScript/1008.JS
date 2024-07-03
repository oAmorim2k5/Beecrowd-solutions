var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let employe = parseInt(lines[0]);
let hoursMonth = parseInt(lines[1]);
let receiveHour = parseFloat(lines[2]);

console.log(`NUMBER = ${employe}\nSALARY = U$ ${(hoursMonth*receiveHour).toFixed(2)}`);