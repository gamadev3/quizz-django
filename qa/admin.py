from django.contrib import admin
from qa.models import Pergunta, Resposta, Categoria, Ranking

@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['enunciado', 'dificuldade']


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ['pergunta', 'resposta', 'e_correta']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ['nome']

admin.site.register(Ranking)