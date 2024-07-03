var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let A = parseFloat(lines[0]*2);
let B = parseFloat(lines[1]*3);
let C = parseFloat(lines[2]*5);

let MEDIA = (A+B+C)/10;
if (MEDIA >= 10){
    MEDIA = 10.0;
    console.log(`MEDIA = 10.0`);
}else{
    console.log(`MEDIA = ${MEDIA.toFixed(5)}`);
};
