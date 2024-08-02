#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const fs = require('fs');
const textA = fs.readFileSync(fileA, 'utf8');
const textB = fs.readFileSync(fileB, 'utf8');

const newText = textA + textB;

fs.appendFile(fileC, newText, function (err) {
  if (err) throw err;
});
