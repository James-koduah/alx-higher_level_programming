#!/usr/bin/node

const args = process.argv;

if (/^\d+$/.test(args[2])) {
  const num = Number(args[2]);
  console.log('My number: ' + num);
} else console.log('Not a number');
