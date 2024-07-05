var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let X = parseInt(lines[0]); //KM
let Y = parseFloat(lines[1]); //FUEL

console.log(`${(X/Y).toFixed(3)} km/l`);