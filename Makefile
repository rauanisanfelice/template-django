-include .env

format:
	@black app --exclude='/migrations/'
	@isort --recursive app

lint:
	@isort --recursive app --check-only
	@flake8 app
	@black app --check --exclude='/migrations/'

clear:
	@printf "Limpando arquivos temporários... "
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.log' -delete

clear-migrations:
	@printf "Limpando arquivos de migrações... "
	@find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	@find . -path "*/migrations/*.pyc"  -delete

requirements-dev:
	@pip install -r requirements/dev.txt

requirements-test:
	@pip install -r requirements/test.txt

packages:
	@printf "Instalando bibliotecas... "
	@venv/bin/pip install -q --no-cache-dir -r requirements/dev.txt
	@echo "Ok"

env-create: env-destroy
	@printf "Criando ambiente virtual... "
	@virtualenv -q venv -p python3.8
	@echo "Ok"

env-destroy:
	@printf "Destruindo ambiente virtual... "
	@rm -rfd env
	@echo "Ok"

install: env-create packages git-config-hooks

copy-example:
	@echo "Copying example files... "
	@cp .env.example .env
	@cp docker-compose.yaml.example docker-compose.yaml
	@echo "OK"

git-config-hooks:
	@git config --local core.hooksPath "$(PWD)/hooks"
	@chmod +x $(PWD)/hooks/*


infra-up:
	@echo "Subindo containers... "
	@docker-compose -f docker-compose.yaml up -d
	@echo "OK"

infra-up-build:
	@docker-compose -f docker-compose.yaml up -d --build

infra-down:
	@docker-compose -f docker-compose.yaml down

infra-rebiuld:
	@docker-compose -f docker-compose.yaml up -d --build --force-recreate


django-clear-database: infra-down clear-migrations infra-rebiuld django-makemigrations django-migrate django-createsuperuser

django-collect-static:
	@printf "Gerando arquivos estáticos... "
	@docker-compose exec app python manage.py collectstatic --noinput
	@echo "OK"

django-makemigrations:
	@printf "Gerando migrações... "
	@docker-compose exec app python manage.py makemigrations --noinput
	@echo "OK"

django-migrate:
	@printf "Importanto migrações... "
	@docker-compose exec app python manage.py migrate --noinput
	@echo "OK"

django-createsuperuser:
	@printf "Criando super usuário... "
	@docker-compose exec -e DJANGO_SUPERUSER_PASSWORD=admin app python manage.py createsuperuser --username admin --email teste@teste.com --noinput
	@echo "OK"

django-test: infra-up
	@printf "Realizando testes... "
	@docker-compose exec app python manage.py test . --noinput

run: infra-up django-collect-static django-migrate django-createsuperuser

coverage: clear
	@DB_HOST=localhost coverage run --source='.' ./app/manage.py test app --noinput
	@coverage report --show-missing
	@coverage xml

sonar-up:
	@docker-compose -f docker/sonarqube/docker-compose.yaml up -d

sonar-down:
	@docker-compose -f docker/sonarqube/docker-compose.yaml down

sonar-scan: coverage sonar-up
	sed -i 's@$(PWD)@\/usr\/src@g' coverage.xml && \
	docker run \
		--rm \
		--network=host \
		-e SONAR_HOST_URL="http://127.0.0.1:9000" \
		-v "$(PWD):/usr/src" \
		sonarsource/sonar-scanner-cli \
		-Dsonar.host.url="http://127.0.0.1:9000" \
		-Dsonar.projectKey=template-django \
		-Dsonar.projectName=template-django
