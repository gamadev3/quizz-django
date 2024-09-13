from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Pergunta(models.Model):

    class Nivel(models.TextChoices):
        FACIL = 'FA', 'Fácil'
        MEDIO = 'ME', 'Médio'
        DIFICIL = 'DI', 'Difícil'

    enunciado = models.TextField()
    dificuldade = models.CharField(max_length=2, choices=Nivel)
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True, related_name='perguntas')

    def __str__(self):
        return self.enunciado


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    resposta = models.TextField()
    e_correta = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.resposta} - Pergunta: {self.pergunta.enunciado}'