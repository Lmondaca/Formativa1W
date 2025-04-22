let cart = {};

function loadCart() {
    const storedCart = localStorage.getItem('cart');
    if (storedCart) {
        cart = JSON.parse(storedCart);
    }
    updateCartDisplay();
}

function saveCart() {
    localStorage.setItem('cart', JSON.stringify(cart));
}

function updateCartDisplay() {
    const cartItems = document.getElementById('cart-items');
    const totalConfirm = document.getElementById('total_confirm');
    const cartCount = document.getElementById('cart-count');

    cartItems.innerHTML = '';
    let total = 0;
    let count = 0;

    for (const [item, details] of Object.entries(cart)) {
        const { price, quantity } = details;
        total += price * quantity;
        count += quantity;

        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item}</td>
            <td>CLP$${price}</td>
            <td>${quantity}</td>
            <td>
                <button class="btn btn-sm btn-danger remove-item" data-item="${item}">Eliminar</button>
            </td>
        `;
        cartItems.appendChild(row);
    }

    cartCount.textContent = count;
    totalConfirm.textContent = `Total: CLP$${total}`;
}

document.addEventListener('click', function (e) {
    if (e.target.closest('.add-to-cart')) {
        const button = e.target.closest('.add-to-cart');
        const item = button.getAttribute('data-item');
        const price = parseInt(button.getAttribute('data-price'));

        if (!cart[item]) {
            cart[item] = { quantity: 0, price: price };
        }
        cart[item].quantity += 1;

        saveCart();
        updateCartDisplay();
    }
});

document.addEventListener('click', function (e) {
    if (e.target.classList.contains('remove-item')) {
        const item = e.target.getAttribute('data-item');
        delete cart[item];
        saveCart();
        updateCartDisplay();
    }
});

document.getElementById('clear-cart').addEventListener('click', function () {
    cart = {};
    saveCart();
    updateCartDisplay();
});

document.addEventListener('DOMContentLoaded', loadCart);