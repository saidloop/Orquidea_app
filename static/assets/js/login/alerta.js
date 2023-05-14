document.getElementById('login-form').addEventListener('submit', function (e) {
  e.preventDefault();
  var url = "/login/";
  var formulario = new FormData(document.getElementById('login-form'));
  console.log(formulario);

  fetch(url, {
      method: 'POST',
      body: formulario,       
  })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
            window.location.href = data.url;
        } else {
            var alerta = document.getElementById('alert-login');
            alerta.style.display = 'block';
            alerta.querySelector('p').innerHTML = data.message;
        }
    });
})



