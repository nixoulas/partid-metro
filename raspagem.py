import requests

res = requests.get('https://www.camara.leg.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoesVotadasEmPlenario?ano=2019&tipo=PEC.txt')

try:
    res.raise_for_status()

    file = open('dados.json', "wb")

    for chunk in res.iter_content(100000):
        file.write(chunk)
except Exception as exc:
    print("Houve um erro: %s" % (exc))
