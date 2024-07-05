var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let R = parseFloat(lines[0]);
const pi = 3.14159;

function calculateVolume(){
    console.log(`VOLUME = ${((4/3)*pi*(R**3)).toFixed(3)}`);
};
calculateVolume()

/*
calculateVol(R);

function calculateVol(){
    var vol = (4/3)*pi*(R**3);
    return vol
};

let volume = calculateVol(volume)

console.log(`VOLUME = ${volume.toFixed(3)}`);
*/