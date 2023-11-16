#!/usr/bin/node

const request = require('request');

async function fetchData () {
  let titleIndex = process.argv[2] - 1;
  if (titleIndex < 1) {
    titleIndex = 1;
  }

  const result = [];

  try {
    const data = await new Promise((resolve, reject) => {
      request('https://swapi-api.alx-tools.com/api/films/', (error, resp, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });

    const films = JSON.parse(data);
    const { characters } = films.results[titleIndex];

    if (!characters) {
      console.log('No Character found!');
      return;
    }

    await Promise.all(
      characters.map(async (link) => {
        try {
          const body = await new Promise((resolve, reject) => {
            request(link, (error, resp, content) => {
              if (error) {
                reject(error);
              } else {
                resolve(content);
              }
            });
          });

          const res = JSON.parse(body);
          result.push(res.name);
        } catch (error) {
          console.error('Error fetching character data:', error);
        }
      })
    );

    result.forEach((xter) => {
      console.log(xter);
    });
  } catch (error) {
    console.error('Error:', error);
  }
}
fetchData();
