#!/usr/bin/node
const myArgs = process.argv[0]
if (!myArgs[0]) {
  console.log('No argument');
} else {
  console.log(myArgs[0]);
}
