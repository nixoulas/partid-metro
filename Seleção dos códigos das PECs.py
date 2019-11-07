from bs4 import BeautifulSoup


try:
    arquivo = open('dados.json')
    soup = BeautifulSoup(arquivo, 'html.parser')

    listcodigo = soup.select('codProposicao')
    for codigos in listcodigo:
        print(codigos.get_text())

except Exception as exc:
    print("Houve um erro: %s" % (exc))