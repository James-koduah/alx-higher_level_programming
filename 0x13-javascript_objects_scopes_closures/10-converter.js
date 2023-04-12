#!/usr/bin/node

exports.converter = function (base) {
  function jj (num) {
    return num.toString(base);
  }
  return jj;
};
