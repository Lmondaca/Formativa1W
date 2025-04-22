

$(document).ready(function () {
    $("#limpiarFormulario").click(function () {
        // $("#formularioRegistro")[0].reset();
        $("input").prop("disabled",false);
        $("#limpiarFormulario").prop("hidden",true);
        $('#boton_mod').prop("disabled",false);
        $(".error").text("");
        
    });


    $("#formularioPerfil").submit(function (event) {
        event.preventDefault();

        $(".error").text("");

        let valid = true;

        
        

        $("input").prop("disabled",true);
        $("#limpiarFormulario").prop("hidden",false);
        $('#boton_mod').prop("disabled",true);
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

       

     

        const fechaNacimiento = new Date($("#fechaNacimiento").val());
        const hoy = new Date();
        const edadMinima = new Date(hoy.getFullYear() - 13, hoy.getMonth(), hoy.getDate());
        if (!$("#fechaNacimiento").val()) {
            $("#errorFecha").text("La fecha de nacimiento es obligatoria.");
            valid = false;
        } else if (fechaNacimiento > edadMinima) {
            $("#errorFecha").text("No puedes tener menos de 13 años.");
            valid = false;
        }
       
        if (valid) {
            alert("Formulario enviado correctamente.");
        }
    });
});