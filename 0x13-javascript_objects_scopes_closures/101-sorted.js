#!/usr/bin/node

const dic = require('./101-data').dict;

let newDic = {};
for (let i in dic) {
	let dicVal = dic[i];
	if (dicVal in newDic) // if the key already exists, just push into it
	{
		newDic[dicVal].push(i);
	}
	else {
		newDic[dicVal] = [];  // if the key does not already exist, create and push
		newDic[dicVal].push(i);
	}
}
console.log(newDic);

