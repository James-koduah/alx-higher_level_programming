#!/usr/bin/node



let args = process.argv.slice(2);
let fs = require('fs')
let data = fs.readFileSync(args[0], 'utf-8')
console.log(data)
