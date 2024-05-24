fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const titles = document.querySelector('#list_movies')

    titles.innerHTML = ''
    for (const element of data.results) {
      const titleName = document.createElement('li')
      titleName.textContent = `${element.title}`
      titles.appendChild(titleName)
    }
  })
