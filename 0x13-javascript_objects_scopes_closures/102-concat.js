#!/usr/bin/node
const fs = require('node:fs')
const fileOne = fs.readFile(process.argv[2], 'utf8',
			    (err, data) => {
				if (err) {
				    console.log(err)
				}})
