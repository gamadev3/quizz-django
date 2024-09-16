let timer;
let segundos = 0;
let minutos = 0;
let horas = 0;

let contador = 0;



function iniciarContador() {
    timer = setInterval(() => {
        atualizarContador,
        contador++,
        document.getElementById('input_contador').value = contador
    }, 1000)
}

function pararContador() {
    clearInterval(timer);
}


function atualizarContador(){
    segundos += 1;
    
    if (segundos == 60) {
        segundos = 0;
        minutos += 1;

        if (minutos == 60) {
            horas += 1;
        }
    }

    document.getElementById('input_contador').innerText = timer;

}

document.addEventListener('DOMContentLoaded', iniciarContador);