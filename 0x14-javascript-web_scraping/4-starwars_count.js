#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';
const baseUrl = apiUrl.endsWith('/') ? apiUrl : `${apiUrl}/`;

request(baseUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  try {
    const films = JSON.parse(body).results;
    const wedgeFilms = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(wedgeFilms.length);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
