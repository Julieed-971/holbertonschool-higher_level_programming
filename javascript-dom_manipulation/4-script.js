const ulElement = document.querySelector('.my_list')
const addItem = document.querySelector('#add_item')
addItem.addEventListener('click', () => {
  const liElement = document.createElement('li')
  liElement.textContent = 'Item'
  ulElement.append(liElement)
})
