* API de Preços de Tapetes

* Descrição

API desenvolvida em Python utilizando FastAPI para consultar preços de tapetes em uma API externa e retornar os dados juntamente com uma data informada pelo usuário.

* Tecnologias utilizadas

 Python
 FastAPI
 Requests
 Uvicorn

* Instalação

* Clone o repositório:

git = https://github.com/gustavonascee/defteste1.git

* Entre na pasta do projeto:

cd defteste1

* Instale as dependências:

pip install fastapi uvicorn requests

* Executando a aplicação

* Execute o comando:

python -m uvicorn main:app --reload

* aplicação ficará disponível em:

http://127.0.0.1:8000

* Documentação Swagger

* A documentação da API pode ser acessada em:

http://127.0.0.1:8000/docs

* Endpoint

* GET /precos

* Parâmetro:

* data (string)

* Exemplo de utilização:

http://127.0.0.1:8000/precos?data=28/05/2024

* Exemplo de resposta

{
"data": "28/05/2024",
"dados": [
{
"id": 1,
"nome": "Triângulo",
"tipo": 2,
"valor_m2": 9.67
}
]
}

//todo o processo foi registrado manualmente em folha de caderno também
