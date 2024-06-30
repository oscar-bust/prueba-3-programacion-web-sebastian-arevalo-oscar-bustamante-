
$(document).ready(function() {
    
    $('#usuario, #contraseña').on('input', function() {
      var campo1 = $('#usuario').val();
      var campo2 = $('#contraseña').val();
  
      if (campo1 !== '' && campo2 !== '') {
        $('#submitt').show();
      } else {
        $('#submitt').hide();
      }
    });
  
    // Evitar la acción por defecto del botón
    $('#submitt').on('click', function(e) {
      e.preventDefault();
      
    });
  });
