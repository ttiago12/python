##faça um for em x, onde cada palavra da lista ficará armazenada
##em x e utiliza o len(para contar as letras) que possui no x
## naquele momento , e isso é retornado como uma lista
def contador_letras(listas_palavras):
    contador = []
    for x in listas_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

##modolo
## caso eu chame esse metodo no outro modulo nçao vai dar certo
##pois eu importei somente o metodo acima
def teste():
    return'teste'

if __name__ == '__main__':
    lista = ['cachorro','gato']
    print(contador_letras(lista))