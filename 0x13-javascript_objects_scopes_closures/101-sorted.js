#!/usr/bin/node

const dic = require('./101-data').dict;

const newDic = {};
for (const i in dic) {
  const dicVal = dic[i];
  if (dicVal in newDic) {
    newDic[dicVal].push(i); // if the key already exists, just push into it
  } else {
    newDic[dicVal] = []; // if the key does not already exist, create and push
    newDic[dicVal].push(i);
  }
}
console.log(newDic);
