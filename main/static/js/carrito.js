document.addEventListener('DOMContentLoaded', () => {
    const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
    const cartItemsElement = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    let total = 0;
  
    cartItems.forEach(item => {
      const li = document.createElement('li');
      li.classList.add('list-group-item');
      li.textContent = `${item.name} - ${item.price}$`;
      cartItemsElement.appendChild(li);
      total += item.price;
    });
  
    cartTotalElement.textContent = total;
  });


  document.addEventListener('DOMContentLoaded', () => {
    const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
    const cartItemsElement = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    let total = 0;
  
    // Función para renderizar el carrito
    function renderCart() {
      cartItemsElement.innerHTML = '';
      total = 0;
      cartItems.forEach(item => {
        const li = document.createElement('li');
        li.classList.add('list-group-item');
        li.textContent = `${item.name} - ${item.price}$`;
        cartItemsElement.appendChild(li);
        total += item.price;
      });
      cartTotalElement.textContent = total;
    }
  
    renderCart();
  
    // Event listener para eliminar un elemento del carrito
    cartItemsElement.addEventListener('click', (e) => {
      if (e.target.classList.contains('delete-item')) {
        const itemId = parseInt(e.target.getAttribute('data-id'));
        const updatedCartItems = cartItems.filter(item => item.id !== itemId);
        localStorage.setItem('cartItems', JSON.stringify(updatedCartItems));
        cartItems = updatedCartItems;
        renderCart();
      }
    });
  
    // Event listener para editar la cantidad de un producto (si se implementa)
    // ...
  
  });
  