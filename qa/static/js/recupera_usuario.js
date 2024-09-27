document.addEventListener('DOMContentLoaded', function() {
    var nomeUsuario = sessionStorage.getItem('usuario')
    var inputUsuario = document.getElementById('txt_usuario')
    if (nomeUsuario) {
        inputUsuario.value = nomeUsuario
    }
})