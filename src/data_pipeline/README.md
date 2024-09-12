# 1. Como rodar
Abra a pasta data_pipeline no terminal

Crie o .env e troque para os dados corretos
```
make copy
```
**Atenção:** Será criado .env na pasta /infra e na pasta /data_pipeline

Rode o comando para iniciar a infra:
```
make up
```
**Atenção:** É necessário que o Docker esteja executando na máquina

Abra um novo terminal

Na pasta data_pipeline, rode o comando para iniciar o projeto:
```
make all
```

Opcional (Permissão):
```
sudo make all
```

Teste os endpoints:
```
POST http://localhost:5000/bucket
Content-Type: application/json

{
    "bucket_name": "test"
}
```

```
GET http://localhost:5000/bucket
Content-Type: application/json
```

# 2. Testes
## Ferramentas utilizadas
- pytest
- unittest
## Como rodar
-       poetry run pytest
## Nível de cobertura
- ferramenta utilizada: pytest cov

Como rodar e gerar html:
-       poetry run pytest --cov=core --cov-report=html

Relatório gerado:
![relatorio-cobertura](<../../assets/coverage.png>)