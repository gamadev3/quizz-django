from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Count
from qa.models import Categoria, Resposta
from datetime import datetime


def exibir_pagina_inicial(request):
    return render(request, 'qa/pagina_inicial.html')

def list_all_qa(request):
    categorias = Categoria.objects.annotate(qtd_perguntas=Count('perguntas'))

    if request.method == 'GET':
        return render(
            request,
            'qa/list_all_qa.html',
            {'categorias': categorias}
        )
    
def listar_perguntas_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    perguntas = categoria.perguntas.all()

    return render(
        request,
        'qa/categoria_detalhes.html',
        {
            'categoria': categoria,
            'perguntas': perguntas
        }
    )

def validar_respostas(request):
    if request.method == 'POST':
        data_envio = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        tempo = request.POST.get('txt_cronometro')
        print(tempo)
        print(data_envio)
        respostas_ids = []
        qtd_respostas_certas = 0

        for key, value in request.POST.items():

            if key.startswith('resposta_'):
                #pergunta_id = key.split('_')[1]
                resposta_id = value
                respostas_ids.append(resposta_id)

        print(respostas_ids)
        for resposta in respostas_ids:
            if Resposta.objects.get(id=resposta).e_correta:
                qtd_respostas_certas += 1

    return render(
        request,
        'qa/resultados.html',
        {
            'qtd_acertos': qtd_respostas_certas,
            'dia_atual': data_envio,
            'tempo': tempo
        }
    )