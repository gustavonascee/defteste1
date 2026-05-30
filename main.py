from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/precos")
def buscar_precos(data: str)
    try:
        resposta = requests.get(
            "https://testedefensoriapr.pythonanywhere.com/precos"
        )

        dados = resposta.json()

        return {
            "data": data,
            "dados": dados
        }

    except:
        return {
            "erro": "Não foi possível consultar a API externa, por favor tente novamente mais tarde"
        }
