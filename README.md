
# 1. Projeto Quizz - Unisagrado

Projeto desenvolvido para o bootcamp da Univerisade do Sagrado Coração de Bauru/SP - 2024.
Curso: Análise e Desenvolvimento de Sistemas

## 1.1. Deploy

Para fazer o deploy desse projeto localmente, certifique-se que tem o Python instalado em sua máquina:

```bash
  python --version
```

1. Baixe o projeto e descompacte em uma pasta ou faça clone do projeto se tiver conhecimentos em git/github.

2. Acesse essa pasta pelo terminal e rode o comando para criar um ambiente virtual:
```bash
  python -m venv .venv
```
3. Instale as dependências do projeto:
```bash
    pip install -r requirements.txt
```
4. Aguarde a instalação e quando acabar, execute os comandos para criar o banco de dados:
```bash
    python manage.py makemigrations
```
```bash
    python manage.py migrate
```

5. Popular o banco de dados:
```bash
    python manage.py loaddata dados.json
```
6. Inicie o servidor:
```bash
    python manage.py runserver
```
7. Abra o seu navegador preferido (google chrome, firefox, edge) e acesse:
```html
    http://127.0.0.1:8000/qa
```



## 1.2. Stack utilizada

**Front-end:** HTML, CSS, JS, Bootstrap

**Back-end:** Python, Django








