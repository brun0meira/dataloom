.PHONY: up install test run

copy:
	cp .env.example .env;
	cd infra; cp .env.example .env

up: 
	cd infra; docker compose up

install:
	poetry install

# test:
# 	poetry run pytest tests

run:
	poetry run python app.py

all: install test run