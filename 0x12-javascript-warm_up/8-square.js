#!/usr/bin/node

const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let m = '';
    for (let j = 0; j < arg; j++) {
      m += 'X';
    }
    console.log(m);
  }
}
