#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const destFile = process.argv[4];

const content1 = fs.readFileSync(file1, 'utf-8');
const content2 = fs.readFileSync(file2, 'utf-8');

fs.writeFileSync(destFile, content1 + content2);
