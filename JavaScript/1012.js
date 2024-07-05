var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split(' ');

let pi = 3.14159;
let A = parseFloat(lines[0]);
let B = parseFloat(lines[1]);
let C = parseFloat(lines[2]);

console.log(`TRIANGULO: ${((A*C)/2).toFixed(3)}`);
console.log(`CIRCULO: ${(pi*(C**2)).toFixed(3)}`);
console.log(`TRAPEZIO: ${((A+B)*(C/2)).toFixed(3)}`);
console.log(`QUADRADO: ${(B**2).toFixed(3)}`);
console.log(`RETANGULO: ${(A*B).toFixed(3)}`);

/*var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split(' ');

const pi = 3.14159;
let A = parseFloat(lines[0]);
let B = parseFloat(lines[1]);
let C = parseFloat(lines[2]);

function  areaRecTriangle()
{
    console.log(`TRIANGULO: ${((A*C)/2).toFixed(3)}`);
};
function  areaCircle()
{
    console.log(`CIRCULO: ${(pi*(C**2)).toFixed(3)}`);
};
function  areaTrapezium()
{
    console.log(`TRAPEZIO: ${((A+B)*(C/2)).toFixed(3)}`);
};
function  areaSquare()
{
    console.log(`QUADRADO: ${(B**2).toFixed(3)}`);
};
function  areaRectangle()
{
    console.log(`RETANGULO: ${(A*B).toFixed(3)}`);
};

areaRecTriangle();
areaCircle();
areaTrapezium();
areaSquare();
areaRectangle();
*/