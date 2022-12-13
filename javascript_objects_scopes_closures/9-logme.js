#!/usr/bin/node
// Prints the number of arguments already printed and the new
// argument value

exports.logMe = function (item) {
  let counter = 0;
  console.log(`${counter}: ${item}`);
  counter++;
};
