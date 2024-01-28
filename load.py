import json


def save_jason(dados):
    with open('dados.json','w') as arquivo_json:
        json.dump(dados,arquivo_json)