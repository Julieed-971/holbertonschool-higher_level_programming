//  fetches the character name
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const character = document.querySelector('#character')

    character.innerHTML = ''
    // display name in HTML tag with id character
    const name = document.createElement('p')
    name.textContent = `${data.name}`
    character.appendChild(name)
  })
