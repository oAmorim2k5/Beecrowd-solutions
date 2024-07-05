var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let timeSeconds = parseInt(lines[0]);
console.log(`${parseInt(timeSeconds/3600)}:${parseInt((timeSeconds%3600)/60)}:${parseInt(((timeSeconds%3600)%60)%60)}`);