#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

for (let i = 2; i < 4; i++) {
  fs.readFile(args[i], 'utf8', (err, data) => {
    if (err) return;
    fs.writeFile(args[4], data, { flag: 'a+' }, err => {
      if (err);
    });
  });
}
