#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;
  const fetchCharacterName = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  };

  const fetchAllCharacterNames = async () => {
    try {
      for (const characterUrl of characters) {
        const name = await fetchCharacterName(characterUrl);
        console.log(name);
      }
    } catch (error) {
      console.error(error);
    }
  };

  fetchAllCharacterNames();
});
