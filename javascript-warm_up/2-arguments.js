#!/usr/bin/node
const args = process.argv;
if (args.length > 3) {
  console.log('Aguments found');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
