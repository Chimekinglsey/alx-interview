#!/usr/bin/node

const request = require('request');
let title_index = process.argv[2] - 1;
if (title_index < 1) {
  title_index = 1;
}

const result = [];
const resp = request('https://swapi-api.alx-tools.com/api/films/', (error, resp, data) => {
  if (error) {
    console.log('Error:', error);
    return;
  }
  const films = JSON.parse(data);
  const characters = films.results[title_index].characters;
  if (!characters) {
    console.log('No Character found!');
    return;
  }
  characters.forEach(link => {
    request(link, (error, resp, body) => {
      if (!error) {
        const res = JSON.parse(body);
        result.push(res.name);
      }
      if (result.length === characters.length) {
        result.forEach(xter => {
          console.log(xter);
        });
      }
    });
  });
});


// #!/usr/bin/node
// /**
//  * Starwars API using async/await
//  */

// const request = require('request');

// async function fetchData () {
//   let titleIndex = process.argv[2] - 1;
//   if (titleIndex < 1) {
//     titleIndex = 1;
//   }

//   try {
//     const data = await new Promise((resolve, reject) => {
//       request('https://swapi-api.alx-tools.com/api/films/', (error, resp, data) => {
//         if (error) {
//           reject(error);
//         } else {
//           resolve(data);
//         }
//       });
//     });

//     const films = JSON.parse(data);
//     const characters = films.results[titleIndex].characters;

//     if (!characters) {
//       console.log('No Character found!');
//       return;
//     }

//     const promises = characters.map(async (link) => {
//       try {
//         const body = await new Promise((resolve, reject) => {
//           request(link, (error, resp, body) => {
//             if (error) {
//               reject(error);
//             } else {
//               resolve(body);
//             }
//           });
//         });

//         const res = JSON.parse(body);
//         return res.name;
//       } catch (error) {
//         console.error('Error fetching character data:', error);
//         return null;
//       }
//     });

//     const result = await Promise.all(promises);

//     result.forEach((xter) => {
//       console.log(xter);
//     });
//   } catch (error) {
//     console.error('Error:', error);
//   }
// }

// fetchData();
