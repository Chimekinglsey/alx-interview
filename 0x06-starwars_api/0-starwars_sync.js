#!/usr/bin/node

const request = require('request')
let title_index = process.argv[2] - 1
if (title_index < 1){
  title_index = 1
}

let result = []
const resp = request('https://swapi-api.alx-tools.com/api/films/',(error, resp, data) =>{
  if(error){
    console.log("Error:", error)
    return
  }
  const films = JSON.parse(data)
  const characters = films['results'][title_index]['characters']
  if (!characters){
    console.log('No Character found!')
    return
  }
  characters.forEach(link => {
    request(link,(error, resp, body) =>{
      if (!error){
        const res = JSON.parse(body)
        result.push(res['name'])
      }
    if (result.length === characters.length){
      result.forEach(xter => {
        console.log(xter)
      })
    }
  })
});
})
