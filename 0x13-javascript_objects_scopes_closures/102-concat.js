#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf8', (err, data) => {
  if (err) return;
  fs.writeFile(args[4], data, { flag: 'a+' }, err => {
    if (err);
  });
});
fs.readFile(args[3], 'utf8', (err, data) => {
  if (err) return;
  fs.writeFile(args[4], data, { flag: 'a+' }, err => {
    if (err);
  });
});
