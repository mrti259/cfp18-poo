PYTHON= ./venv/bin/python
PIP= ./venv/bin/pip
FLASK= ./venv/bin/flask

.PHONY: tests

help:
	@cat HELP

setup:
	python3 -m venv venv
	$(PIP) install -r requirements.txt

tests:
	$(PYTHON) -m unittest tests.py

run:
	$(FLASK) run

init_db:
	$(FLASK) db init
	git init migrations

migration:
	$(FLASK) db migrate

upgrade:
	$(FLASK) db upgrade

requirements:
	$(PIP) freeze > requirements.txt

shell:
	$(FLASK) shell
