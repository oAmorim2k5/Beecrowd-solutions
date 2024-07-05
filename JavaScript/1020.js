var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let entry = parseInt(lines[0]);
console.log(`${parseInt(entry/365)} ano(s)\n${parseInt((entry%365)/30)} mes(es)\n${parseInt(((entry%365)%30)%30)} dia(s)`);