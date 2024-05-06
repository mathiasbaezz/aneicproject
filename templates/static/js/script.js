$(document).ready(function(){
  $('#phone-number').mask('0000-000000');
 })


document.addEventListener('DOMContentLoaded', function() {
        var form = document.querySelector('form');
        form.addEventListener('submit', function(event) {
            var password = document.getElementById('password').value;
            var confirmPassword = document.getElementById('confirm-password').value;

            if (password !== confirmPassword) {
                alert('Las contraseñas no coinciden. Por favor, inténtalo de nuevo.');
                event.preventDefault(); // Evita que el formulario se envíe
            }
        });
    });

document.addEventListener('DOMContentLoaded', function() {
        var form = document.querySelector('form');

        form.addEventListener('submit', function(event) {
            var requiredFields = form.querySelectorAll('[required]');
            var isValid = true;

            requiredFields.forEach(function(field) {
                if (field.value.trim() === '') {
                    isValid = false;
                }
            });

            if (!isValid) {
                alert('Por favor, completa todos los campos obligatorios.');
                event.preventDefault(); // Evita que el formulario se envíe
            }
        });
    });

