fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then((response) => response.json())
  .then((data) => {
    const helloElement = document.querySelector('#hello')

    helloElement.innerHTML = ''
    const greeting = document.createElement('p')
    greeting.textContent = `${data.hello}`
    helloElement.appendChild(greeting)
  })
