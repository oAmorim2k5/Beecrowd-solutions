var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let N = parseInt(lines[0]);

if (0 < N < 1000000){
    console.log(N);
    console.log(`${parseInt(N/100)} nota(s) de R$ 100,00`, );
    N%=100;
    console.log(`${parseInt(N/50)} nota(s) de R$ 50,00`);
    N%=50;
    console.log(`${parseInt(N/20)} nota(s) de R$ 20,00`);
    N%=20;
    console.log(`${parseInt(N/10)} nota(s) de R$ 10,00`);
    N%=10;
    console.log(`${parseInt(N/5)} nota(s) de R$ 5,00`);
    N%=5;
    console.log(`${parseInt(N/2)} nota(s) de R$ 2,00`);
    N%=2;
    console.log(`${parseInt(N/1)} nota(s) de R$ 1,00`);
    N%=1;
};