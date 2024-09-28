from django.urls import path
from qa import views
 
urlpatterns = [
    path('', views.exibir_pagina_inicial, name='pagina_inicial'),
    path('qa/', views.list_all_qa, name='list_qa'),
    path('qa/categorias/<int:id_categoria>/', views.listar_perguntas_categoria, name='perguntas_por_categoria'),
    path('qa/validar/', views.validar_respostas, name='validar_respostas'),
    path('qa/filtrar/', views.filtrar_categorias, name='filtrar_categorias'),   
    path('qa/salvar/', views.salvar_resultado, name="salvar_resultado"),
] 