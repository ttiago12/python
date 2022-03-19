import requests

##UTILIZANDO O METODO GET FAZ UM REQUISICAO   HTTP
##VIACEP = API QUE CONSULTA DADOS DE UM CEP
def retorna_dados_cep(cep):
    ##RESPONSE É A VARIAVEL UTILIZAR PARA CHAMAR O METODO
    #response = requests.get('https://viacep.com.br/ws/29278987/json/')

    ##colocando chaves para puxar o cep inserido, além do
    ##.format(cep)
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    ##SE RETORNAR 200 = SUCESSO 400 = ERRO
    #print(response.status_code)

    ##IMPRIMIR TODOS O TEXTO DA PAGINA
    ##verificando o tipo do resultado retornado
    print(response.text)
    print(type(response.text))

    ##TRAZ NO FORMATO DE DICIONARIO
    ##verificando o tipo do resultado retornado
    print(response.json())
    print(type(response.json()))

    ## estando no formato de dicionario eu consigo
    dados_cep = response.json()
    print('TRAZENDO SOMENTE O LOGRADOURO')
    print(dados_cep['logradouro'])
    print('TRAZENDO A LOCALIDADE')
    print(dados_cep['localidade'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

##fazendo requisição de um site normal
def retorna_response(url):

    ## retorna o html de uma páginaaaaaaaaa
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    #retorna_dados_cep('29278987')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['abilities'])
    response = retorna_response('https://fortux.netlify.app/')
    print(response)