const header = document.querySelector('header')
const updateHeader = document.querySelector('#update_header')
updateHeader.addEventListener('click', () => {
  header.textContent = 'New Header!!!'
})
