
const urlParams = new URLSearchParams(window.location.search);
const isAdmin = urlParams.has('admin');

document.getElementById('adminLink').style.display = isAdmin ? 'block' : 'none';

document.getElementById('adminBtn').textContent = isAdmin ? 'Modo Usuario' : 'Modo Admin';

document.getElementById('adminBtn').href = isAdmin ? window.location.pathname : '?admin=true';


document.addEventListener('DOMContentLoaded', () => {
    const categoria = document.title;
    const games = JSON.parse(localStorage.getItem('games')) || [];

    const filteredGames = games.filter(game =>
        game.category.toLowerCase() === categoria.toLowerCase()
    );

    const container = document.getElementById('agregar-juego');

    filteredGames.forEach(game => {
        container.innerHTML += `
            <div class="descripcionJuegos1 bg-dark p-4 rounded shadow mb-4 card">
                <img src="${game.image}" alt="${game.name}" class="img-fluid rounded shadow mb-3">
                <div class="card-body">
                <h2 class="text-white card-title">${game.name}</h2>
                <p class="text-white card-text">${game.description}</p>
                <div class="precio_boton d-flex justify-content-between align-items-center">
                    <h2 class="text-white card-title" hidden="true">${game.name}</h2>
                        <h2 class="precio_valor" hidden="true">${game.price}</h2>
                    <h4 class="text-white m-0"><span>CLP$</span> ${new Intl.NumberFormat("es-CL", { style: "currency", currency: "CLP" }).format(game.price)}</h4>
                    <button type="button" class="btn btn-primary add-to-cart">Comprar</button>
                </div>
                </div>
            </div>
        `;
    });
});