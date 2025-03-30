$(document).ready(function(){
    $('#form_nuevojuego').submit(function(event){
        event.preventDefault();

        $('#categoria-error').text('')
        $('#nombre-error').text('')
        $('#descripcion-error').text('')
        $('#precio-error').text('')
        $('#imagen-error').text('')

        if($('#categoria').val() === '') {
            $('#categoria-error').text('Por favor, ingresa una categoría')
            return;
        }

        if($('#nombre').val() === '') {
            $('#nombre-error').text('Por favor, ingresa un nombre')
            return;
        }

        if($('#descripcion').val() === '') {
            $('#descripcion-error').text('Por favor, ingresa una descripción')
            return;
        }

        if($('#precio').val() === '') {
            $('#precio-error').text('Por favor, ingresa un precio')
            return;
        }

        if($('#imagen').val() === '') {
            $('#imagen-error').text('Por favor, ingresa una imagen')
            return;
        }

        this.submit();
    });
})