##tratamento de execao aula11
lista = [1,10]

#CONCEITOS DO FINALY - DANDO ERRO OU NAO O TRECHO É EXECUTADO
print('\\\\\\\ABRINDO ARQUIVO')
arquivo = open('teste.txt', 'r')

try:

    texto = arquivo.read()
    ##gerando o erro
    divisao = 10/0
    numero = lista[1]
    #x = a
    print('\\\\\\\\\FECHANDO ARQUIVO')
    arquivo.close()
except ZeroDivisionError:
    print('Não é possivel realizar uma divisao por zero')
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
##Executa quando não houve exceção
else:
    print('EXECUTA QUANDO NAO TEM EXCEÇÃO')
finally:
    ##sepre executa
    print('/////FECHANDO ARQUIVO')
    arquivo.close()