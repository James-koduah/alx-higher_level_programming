#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const data = fs.readFileSync(args[0], 'utf-8');
console.log(data);
