document.getElementById('createUser').addEventListener('submit', function (e) {
    e.preventDefault();
    var url = "/crear_usuario";
    var formulario = new FormData(document.getElementById('createUser'));
    console.log(formulario);

    fetch(url, {
        method: 'POST',
        body: formulario,       
    })
        .then(response => response.json())
        .then(data => {
            
            if (data.ok) {
                swal.fire({
                    title: 'Success',
                    text: data.message,
                    icon: 'success',
                    confirmButtonText: 'Cool'
                })
                    .then(function () {
                        window.location.href = "/home";
                    })
            }
        });
})