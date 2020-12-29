![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rauanisanfelice/template-django.svg)
![GitHub top language](https://img.shields.io/github/languages/top/rauanisanfelice/template-django.svg)
![GitHub pull requests](https://img.shields.io/github/issues-pr/rauanisanfelice/template-django.svg)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/rauanisanfelice/template-django)
![GitHub contributors](https://img.shields.io/github/contributors/rauanisanfelice/template-django.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/rauanisanfelice/template-django.svg)

![GitHub stars](https://img.shields.io/github/stars/rauanisanfelice/template-django.svg?style=social)
![GitHub followers](https://img.shields.io/github/followers/rauanisanfelice.svg?style=social)
![GitHub forks](https://img.shields.io/github/forks/rauanisanfelice/template-django.svg?style=social)

# Template django

Tempalte Django 3.0.7

1. Virtual env;
2. Dependências;
3. Criando arquivo .env;
4. Baco de dados (caso não tenha);
    1. Configurando o pgAdmin;
5. Migrando conf. para o BD;
5. Inicializando servidor;

### Virtual env
```
virtualenv -p python3 env
source env/bin/activate
```

### Dependências
```
pip3 install -r requirements.txt
```

### Criando arquivo .env

Copie o conteúdo do arquivo env-example e crie um novo arquivo .env, cole o conteúdo.

### Baco de dados (caso não tenha)
```
docker-compose up -d
```

#### Configurando o pgAdmin

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


### Migrando conf. para o BD
```
python manage.py migrate
```

### Inicializando servidor

```
python manage.py runserver 8000 --noreload
```

> http://localhost:8000/admin
