#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const url = args[0];
request(url, (error, response, body) => {
  if (error) console.log(error);
  let res = 0;
  body = JSON.parse(body);
  const results = body.results;
  for (const item of results) {
    const characters = item.characters;
    for (let i = 0; i < characters.length; i++) {
      const item = characters[i];
      const itemLen = item.length;
      let str = '' + item[itemLen - 3];
      str += item[itemLen - 2];
      if (str === '18') res++;
    }
  }
  console.log(res);
});
