
$(document).ready(function(){
  $("#form1").submit(function(event){
    var name = $("#name").val();
    var lastName = $("#lastName").val();
    var email = $("#email").val();
    var password = $("#password").val();
    var isValid = true; 
    if(name == "") {
      $("#advertenciaNombre").text("Por favor, ingrese su nombre.");
      isValid = false;
    } else {
      $("#advertenciaNombre").text(""); 
    }

    
    if(lastName == "") {
      $("#advertenciaApellido").text("Por favor, ingrese su apellido.");
      isValid = false;
    } else {
      $("#advertenciaApellido").text(""); 
    }

    
    if(email == "") {
      $("#advertenciaCorreo").text("Por favor, ingrese su correo electrónico.");
      isValid = false;
    } else {
      $("#advertenciaCorreo").text(""); 
    }

    
    if(password == "") {
      $("#contraseñaAdvertencia").text("Por favor, ingrese su contraseña.");
      isValid = false;
    } else {
      $("#contraseñaAdvertencia").text("");
    }

    
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email != "" && !emailPattern.test(email)) {
      $("#emailWarning").text("Por favor, ingrese un correo electrónico válido.");
      isValid = false;
    }

  
    if(!isValid) {
      event.preventDefault();
    } else {
      alert("Registrado con exito");
    }
  });
});






 /* Aqui hay una funcion que consiste en añadir productos al carrito*/ 




 

 $(document).ready(function() {
  // Función para añadir productos al carrito
  $('.add-to-cart').click(function(e) {
    e.preventDefault();
    const name = $(this).data('name');
    const price = parseFloat($(this).data('price'));

    // Obtener los productos actuales del carrito del localStorage
    let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

    // Agregar el nuevo producto al carrito
    cartItems.push({ name, price });

    // Actualizar el localStorage
    localStorage.setItem('cartItems', JSON.stringify(cartItems));

    // Mostrar mensaje de éxito (puedes cambiar esto por una alerta Bootstrap si lo deseas)
    alert(`${name} ha sido añadido al carrito`);

    // Redireccionar a la página de herramientas
    window.location.href = "{% url 'herramientas' %}";
  });
});






