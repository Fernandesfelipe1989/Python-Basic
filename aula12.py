import requests


def retorna_dados_cep(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    dados_cep = response.json()
    return dados_cep


def retorna_dados_pokemon(pokemon):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(pokemon))
    return response.json()


def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    print(retorna_dados_cep("18017180"))
    dados_pokemon = retorna_dados_pokemon("pikachu")
    print(dados_pokemon['sprites'])
    print(retorna_response("https://globallabs.academy/"))