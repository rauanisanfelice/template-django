![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rauanisanfelice/template-django.svg)
![GitHub top language](https://img.shields.io/github/languages/top/rauanisanfelice/template-django.svg)
![GitHub pull requests](https://img.shields.io/github/issues-pr/rauanisanfelice/template-django.svg)
![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/rauanisanfelice/template-django.svg)
![GitHub contributors](https://img.shields.io/github/contributors/rauanisanfelice/template-django.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/rauanisanfelice/template-django.svg)

![GitHub stars](https://img.shields.io/github/stars/rauanisanfelice/template-django.svg?style=social)
![GitHub followers](https://img.shields.io/github/followers/rauanisanfelice.svg?style=social)
![GitHub forks](https://img.shields.io/github/forks/rauanisanfelice/template-django.svg?style=social)

# Template django

Tempalte Django 3.0

# Instruções

1. Ambiente Python;
2. Instalando dependências;
3. Inicialização dos container;
    1. Configurando o pgAdmin;
4. Iniciar o servidor.

## Ambiente Python

```
virtualenv -p python3 env
source env/bin/activate
```

## Instalando dependências:

```
pip3 install -r requirements.txt
```

### Inicialização dos container

```
docker-compose up -d
```

#### Configurando o pgAdmin;

Acesse o link:

[pgAdmin](http://localhost:80)

Realize o login:
>User: admin  
>Pass: admin

Clique em: Create >> Server

Conecte no Banco com os seguintes parametros:  

Name: #nome desejado#  
>Host: postgre
>Port: 5432  
>DB  : postgres  
>User: admin  
>Pass: docker123

### Iniciar o servidor.

```
python manage.py runserver 8000 --noreload
```

[Site](http://localhost:8000)


### Novo Aplicativo.
```
python manage.py startapp [nome]
```

Alterar *[nome]* pelo nome do novo aplicativo.
