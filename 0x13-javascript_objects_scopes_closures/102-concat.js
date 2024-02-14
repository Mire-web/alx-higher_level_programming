#!/usr/bin/node
const fs = require('fs')
let fileOne = fs.readFile(process.argv[2], 'utf8', (err, data) => {
    fs.appendFile(process.argv[3], data, (err) => {
	console.log(err);
    });
})
console.log(fileOne)
