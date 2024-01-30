import json


def save_jason(dados):
    json_str = json.dumps(dados,ensure_ascii=False)
    with open("Dados/dados.json", "w") as arquivo:
        arquivo.write(json_str)