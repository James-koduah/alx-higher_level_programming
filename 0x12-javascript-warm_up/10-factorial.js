#!/usr/bin/node

function factorial (num) {
  let total = 0;
  if (num > 1) {
    total += factorial(num - 1);
  }
  return num + total;
}

let arg = Number(process.argv[2]);

if (isNaN(arg)) {
  arg = 1;
}
console.log(factorial(arg));
