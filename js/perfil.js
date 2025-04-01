

$(document).ready(function () {
    $("#limpiarFormulario").click(function () {
        $("#formularioRegistro")[0].reset();
        $(".error").text("");
    });


    $("#formularioRegistro").submit(function (event) {
        event.preventDefault();

        $(".error").text("");

        let valid = true;

        
        $("input").prop("disabled",false);
        if ($("#nombreCompleto").val().trim() === "") {
            $("#errorNombre").text("El nombre completo es obligatorio.");
            valid = false;
        }

        if ($("#nombreUsuario").val().trim() === "") {
            $("#errorUsuario").text("El nombre de usuario es obligatorio.");
            valid = false;
        }

        const correo = $("#correo").val().trim();
        const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (correo === "") {
            $("#errorCorreo").text("El correo electrónico es obligatorio.");
            valid = false;
        } else if (!regexCorreo.test(correo)) {
            $("#errorCorreo").text("El correo electrónico no es válido.");
            valid = false;
        }

        const clave = $("#clave").val();
        const regexClave = /^(?=.*[A-Z])(?=.*\d).{6,18}$/;
        if (clave === "") {
            $("#errorClave").text("La contraseña es obligatoria.");
            valid = false;
        } else if (!regexClave.test(clave)) {
            $("#errorClave").text("La contraseña debe tener entre 6 y 18 caracteres, al menos una mayúscula y un número.");
            valid = false;
        }

        const repetirClave = $("#repetirClave").val();
        if (repetirClave === "") {
            $("#errorRepetirClave").text("Debes repetir la contraseña.");
            valid = false;
        } else if (repetirClave !== clave) {
            $("#errorRepetirClave").text("Las contraseñas no coinciden.");
            valid = false;
        }

        const fechaNacimiento = new Date($("#fechaNacimiento").val());
        const hoy = new Date();
        const edadMinima = new Date(hoy.getFullYear() - 13, hoy.getMonth(), hoy.getDate());
        if (!$("#fechaNacimiento").val()) {
            $("#errorFecha").text("La fecha de nacimiento es obligatoria.");
            valid = false;
        } else if (fechaNacimiento > edadMinima) {
            $("#errorFecha").text("Debes tener al menos 13 años para registrarte.");
            valid = false;
        }
        $("#nombreCompleto").prop('disable', true);
        if (valid) {
            alert("Formulario enviado correctamente.");
        }
    });
});