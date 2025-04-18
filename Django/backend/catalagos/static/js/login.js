$(document).ready(function () {
    $("#limpiarFormulario").click(function () {
        $("#formularioRegistro")[0].reset();
        $(".error").text("");
    });

    $("#formularioRegistro").submit(function (event) {
        event.preventDefault();
        
        $(".error").text("");

        let valid = true;

        $("input").disabled =false;

        if ($("#nombreUsuario").val().trim() === "") {
            $("#errorUsuario").text("El nombre de usuario es obligatorio.");
            valid = false;
        }


        const clave = $("#clave").val();
        const regexClave = /^(?=.*[A-Z])(?=.*\d).{6,18}$/;
        if (clave === "") {
            $("#errorClave").text("La contraseña es obligatoria.");
            valid = false;
        } else if ('admin123' !== clave) {
            $("#errorClave").text("Contraseña incorrecta, intente nuevamente.");
            valid = false;
        }

        // const repetirClave = $("#repetirClave").val();
        // if (repetirClave === "") {
        //     $("#errorRepetirClave").text("Debes repetir la contraseña.");
        //     valid = false;
        // } else if (repetirClave !== clave) {
        //     $("#errorRepetirClave").text("Las contraseñas no coinciden.");
        //     valid = false;
        // }

       

        if (valid) {
            
            
            window.location.href = 'index.html';
        }
      
    });
});