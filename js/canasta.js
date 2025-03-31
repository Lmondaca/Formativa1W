let cart = {};
let valor_cart ={};

function updateCartDisplay() {
    let count = Object.values(cart).reduce((a, b) => a + b, 0);
    let total = Object.values(valor_cart).reduce((a, b) => a + b, 0);
    if (count > 0) {
        $('#cart-count').text(count).removeClass('d-none');
    } else {
        $('#cart-count').addClass('d-none');
    }
    let cartItems = $('#cart-items');
    let total_confirm = $('#total_confirm');
    total_confirm.empty();
    total_confirm.append(`
        <div class="row g-3 text-white">
        <div class="col-md-6">
        <h4 class="boton_confirm">Total: ${new Intl.NumberFormat("es-CL", {style:"currency", currency:"CLP"}).format(total)}</h4></div>
       
       <div class="col-md-6"> <button class="btn btn-primary boton_confirm">Confirmar Compra</button></div>
         </div>
       `);
     cartItems.empty();
    Object.keys(cart).forEach(item => {
        cartItems.append(`
            <li class="list-group-item d-flex justify-content-between align-items-center bg-dark text-white">
            <div class="col-md-3">${item}</div> <div class="col-md-3"><span class="badge bg-primary rounded-pill">${cart[item]}</span></div>
            <div class="col-md-3">${new Intl.NumberFormat("es-CL", {style:"currency", currency:"CLP"}).format(valor_cart[item]/cart[item])}</div>
            <button class="btn btn-danger btn-sm remove-item" data-item="${item}">❌</button>
        </li>`);
        
    });
    
}

$(document).on('click', '.add-to-cart', function () {
    let product = $(this).siblings('.card-title').text();
    let valor = $(this).siblings('.precio_valor').text();
    cart[product] = (cart[product] ||0) + 1;
    valor_cart[product]=(valor_cart[product]||0)+ parseInt(valor);
    updateCartDisplay();
});

$(document).on('click', '.remove-item', function () {
    let product = $(this).data('item');
    if (cart[product] > 1) {
        valor_cart[product]-=valor_cart[product]/cart[product];
        cart[product]--;
    } else {
        delete cart[product];
        delete valor_cart[product]
    }
    updateCartDisplay();
});



