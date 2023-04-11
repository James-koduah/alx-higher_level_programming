#!/usr/bin/node

function factorial (num) {
  if (num > 1) {
   return num *= factorial(num - 1);
  } else return 1;
}

let arg = Number(process.argv[2]);

if (isNaN(arg)) {
  arg = 1;
}
console.log(factorial(arg));
