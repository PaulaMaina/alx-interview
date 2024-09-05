#!/usr/bin/node

const req = require('request');

req('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function(error, res, body) {
  if (error) throw error;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
const exactOrder = (actors, p) => {
  if (p === actors.length) return;
  req(actors[p], function(error, res, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    exactOrder(actors, p + 1);
  });
};
