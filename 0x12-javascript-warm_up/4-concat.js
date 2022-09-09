#!/usr/bin/node

// script that prints two arguments passed to it, in the following format: “ is ”

if (typeof process.argv[2] !== 'undefined' && typeof process.argv[3] !== 'undefined') {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (typeof process.argv[3] === 'undefined') {
  console.log(process.argv[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
