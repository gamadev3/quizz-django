from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Count
from qa.models import Categoria, Resposta, Pergunta
from datetime import datetime

  
def save_result(request):
    if request.method == 'POST':
        data = request.POST.get('hidden_data')
        acertos = request.POST.get('hidden_acertos')
        tempo = request.POST.get('hidden_tempo')

        return render(request, 'qa/result_saved.html', {
            'data': data,
            'acertos': acertos,
            'tempo': tempo,
        })


def filtrar_categorias(request):
    nivel_dificuldade = request.GET.get('nivel_dificuldade')

    if nivel_dificuldade:
        categorias = Categoria.objects.filter(nivel_dificuldade=nivel_dificuldade).annotate(qtd_perguntas=Count('perguntas'))
    else:
        categorias = Categoria.objects.annotate(qtd_perguntas=Count('perguntas'))

    return render(request, 'qa/categorias_filtradas.html', {
        'categorias': categorias,
        'nivel_dificuldade': nivel_dificuldade
    })


def exibir_pagina_inicial(request):
    if request.method == 'GET':
        niveis = Pergunta.Nivel.choices


    return render(request, 'qa/pagina_inicial.html', {'niveis': niveis})


def list_all_qa(request):
    categorias = Categoria.objects.annotate(qtd_perguntas=Count('perguntas'))
    return render(request, 'qa/list_all_qa.html', {'categorias': categorias})


def listar_perguntas_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    perguntas = categoria.perguntas.all()
    return render(request, 'qa/categoria_detalhes.html', {
        'categoria': categoria,
        'perguntas': perguntas
    })


def validar_respostas(request):
    if request.method == 'POST':
        data_envio = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        tempo = request.POST.get('txt_cronometro')
        respostas_ids = []
        qtd_respostas_certas = 0

        for key, value in request.POST.items():
            if key.startswith('resposta_'):
                respostas_ids.append(value)

        for resposta_id in respostas_ids:
            resposta = get_object_or_404(Resposta, id=resposta_id)
            if resposta.e_correta:
                qtd_respostas_certas += 1

        return render(request, 'qa/resultados.html', {
            'qtd_acertos': qtd_respostas_certas,
            'dia_atual': data_envio,
            'tempo': tempo
        })
    else:
        return HttpResponse("Método inválido", status=400) 

