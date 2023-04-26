#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  let count = 0;
  JSON.parse(body).results.forEach((result) => {
    count += result.characters.filter((wedgeUrl) => wedgeUrl.includes('18')).length;
  });
  console.log(count);
});
