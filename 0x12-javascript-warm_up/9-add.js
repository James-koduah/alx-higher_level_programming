#!/usr/bin/node

const nua = Number(process.argv[2]);
const nub = Number(process.argv[3]);

function add (a, b) {
  return a + b;
}
if (isNaN(nua) || isNaN(nub)) {
  console.log('NaN');
} else console.log(add(nua, nub));
