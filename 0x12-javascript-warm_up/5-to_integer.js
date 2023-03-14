#!/usr/bin/node
arg = process.argv[2]
if(!(isNaN(arg))) {
	console.log(`My number: ${Number.parseInt(arg, 10)}`);
} else {
	console.log("Not a number")
}
