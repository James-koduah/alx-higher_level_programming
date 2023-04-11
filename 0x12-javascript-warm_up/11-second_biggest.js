#!/usr/bin/node

function secBig (arg) {
  arr = [...arg];
  let max = [0, 0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max[0]) {
      max[0] = arr[i];
      max[1] = i;
    }
  }
  arr[max[1]] = 0;
  max = [0, 0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max[0]) {
      max[0] = arr[i];
      max[1] = i;
    }
  }
  console.log(max[0]);
}
let arr = [];
for (let i = 2; i < process.argv.length; i++) {
  arr.push(Number(process.argv[i]));
}
secBig(arr);
