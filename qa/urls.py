from django.urls import path
from qa import views

urlpatterns = [
    path('qa/', views.list_all_qa, name='list_qa'),
    path('qa/categorias/<int:id_categoria>/', views.listar_perguntas_categoria, name='perguntas_por_categoria'),
    path('qa/validar/', views.validar_respostas, name='validar_respostas')
]