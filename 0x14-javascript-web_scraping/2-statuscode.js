#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

request(args[0]).on('response', (e) => {
  console.log('code: ' + e.statusCode);
});
