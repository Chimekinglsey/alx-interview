This is a challenge to access the StarWars API and dynamically return names of characters
#!/usr/bin/node

const request = require('request');

async function fetchCharacterData (link) {
  return new Promise((resolve, reject) => {
    request(link, (error, resp, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

async function fetchData (movieId) {
  try {
    const filmsResponse = await new Promise((resolve, reject) => {
      request('https://swapi-api.alx-tools.com/api/films/', (error, resp, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(data));
        }
      });
    });

    const characters = filmsResponse.results[movieId - 1]?.characters;

    if (!characters) {
      console.log('No characters found for the specified movie ID.');
      return;
    }

    for (const link of characters) {
      try {
        const characterName = await fetchCharacterData(link);
        console.log(characterName);
      } catch (error) {
        console.error('Error fetching character data:', error);
      }
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID as a command line argument.');
} else {
  fetchData(movieId);
}
