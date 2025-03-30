$(document).ready(function() {
    $('#form_nuevojuego').submit(function(event) {
        event.preventDefault();
        $('.text-danger').text('');
        
        const categoria = $('#categoria').val();
        const nombre = $('#nombre').val().trim();
        const descripcion = $('#descripcion').val().trim();
        const precio = $('#precio').val();
        const imagen = $('#imagen')[0].files[0];

        let hasErrors = false;

        if (!categoria) {
            $('#categoria-error').text('Selecciona una categoría válida');
            hasErrors = true;
        }

        if (!nombre) {
            $('#nombre-error').text('Nombre requerido');
            hasErrors = true;
        }

        if (!descripcion || descripcion.length < 50) {
            $('#descripcion-error').text('Descripción mínima 50 caracteres');
            hasErrors = true;
        }

        if (!precio || isNaN(precio) || precio < 1000) {
            $('#precio-error').text('Precio inválido (mínimo $1.000)');
            hasErrors = true;
        }

        if (!imagen) {
            $('#imagen-error').text('Selecciona una imagen');
            hasErrors = true;
        }

        if (hasErrors) return;

        // convertir imagen a Base64
        const reader = new FileReader();
        reader.onload = function(e) {
            const newGame = {
                id: Date.now(),
                name: nombre,
                category: categoria,
                description: descripcion,
                price: parseFloat(precio),
                image: e.target.result,
                date: new Date().toISOString()
            };

            const games = JSON.parse(localStorage.getItem('games')) || [];
            games.push(newGame);
            localStorage.setItem('games', JSON.stringify(games));

            alert('Juego agregado exitosamente!');
            window.location.href = categoria.toLowerCase() + '.html';
        };
        reader.readAsDataURL(imagen);
    });
});