##tratamento de execao aula11
lista = [1,10]

try:
    ##gerando o erro
    divisao = 10/1
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print('Não é possivel realiar uma divisao por zero')
except IndexError:
    print('Erro ao acessar um indice invalida da lista')
## bsae mãe , contem todas as exeções
##gravanado a mensagem de erro que vem do da Base , no ex
except BaseException as ex:
    print(ex)
    print('erro desconhecido : {}'.format(ex))
##tratamento de erro generico
except:
    print('Erro  desconhecido')