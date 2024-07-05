var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let hour = parseInt(lines[0]);
let km = parseInt(lines[1]);

console.log(`${parseFloat((hour*km)/12).toFixed(3)}`);