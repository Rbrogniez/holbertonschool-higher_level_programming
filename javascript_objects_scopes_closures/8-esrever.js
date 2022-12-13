#!/usr/bin/node
// Write a function that returns the reversed version of a list

exports.esrever = function (list)
{
	var NewList = [];
	for (var i = list.length - 1; i >= 0; i--) {
	  NewList.push(list[i]);
	}
	return NewList;
  }
