#!/usr/bin/node
const fs = require('fs');

// Get file paths from command line arguments
const [, , fileA, fileB, fileC] = process.argv;

// Read content of fileA
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) throw err;

  // Read content of fileB
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) throw err;

    // Concatenate contents of fileA and fileB
    const concatenatedContent = `${dataA}${dataB}`;

    // Write concatenated content to fileC
    fs.writeFile(fileC, concatenatedContent, (err) => {
      if (err) throw err;
      console.log(`Concatenated content has been written to ${fileC}`);
    });
  });
});
