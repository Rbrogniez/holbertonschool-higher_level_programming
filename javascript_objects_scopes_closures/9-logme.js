#!/usr/bin/node
exports.logMe = function (item) {
	// Create a counter variable to keep track of the number of arguments printed
	let counter = 0;

	// Return a function that will be called each time the logMe function is called
	return function() {
	  // Increment the counter variable
	  counter++;
	  // Print the current count and the current argument value
	  console.log(`${counter}: ${item}`);
	}
  }
