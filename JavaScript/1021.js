/*var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let N = parseInt(lines[0]);
let contOne = 0;

if (0 < N < 1000000){
    console.log("NOTAS:");
    console.log(`${parseInt(N/100)} nota(s) de R$ 100.00`);
    N%=100;
    console.log(`${parseInt(N/50)} nota(s) de R$ 50.00`);
    N%=50;
    console.log(`${parseInt(N/20)} nota(s) de R$ 20.00`);
    N%=20;
    console.log(`${parseInt(N/10)} nota(s) de R$ 10.00`);
    N%=10;
    console.log(`${parseInt(N/5)} nota(s) de R$ 5.00`);
    N%=5;
    console.log(`${parseInt(N/2)} nota(s) de R$ 2.00`);
    N%=2;
    console.log("MOEDAS:");
    console.log(`${parseFloat(N/1)} moeda(s) de R$ 1.00`);
    N%=1;
    console.log(`${parseFloat(N/0.50)} moeda(s) de R$ 0.50`);
    N%=0.50;
    console.log(`${parseFloat(N/0.25)} moeda(s) de R$ 0.25`);
    N%=0.25;
    console.log(`${parseFloat(N/0.10)} moeda(s) de R$ 0.10`);
    N%=0.10;
    console.log(`${parseFloat(N/0.05)} moeda(s) de R$ 0.05`);
    N%=0.05;
    if(parseFloat(N).toFixed(4) >= 0.01){
        N-=0.01;
        contOne+=1;
    };
    console.log(`${parseInt(contOne)} moeda(s) de R$ 0.01`);
};
*/