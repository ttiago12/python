# # ## conjunto utiliza chaves exemplo : nome_conjunto : {valor,valor2}
# # # ##Não permite duplicidade
# # #
# # # conjunto = {1,2,3,4,4,5,5}
# # # print (conjunto)
# # #
# # # ##adicionar valor ao conjunto
# # # conjunto.add(12)
# # # ##remover elemento do conjunto
# # # conjunto.discard(2)
# #
# # print (conjunto)

#unicao de conjuntos
conjunto  = {1,2,3,4,5,9,12,15}
conjunto2 = {1,2,7,6,7,8,5,6,10}

print('CONJUNTO 1 == {}'.format(conjunto))
print('CONJUNTO 2 == {}'.format(conjunto2)+'\n')

conjunto_uniao = conjunto.union(conjunto2)
print('CONJUNTO UNIÃO == {}'.format(conjunto_uniao))

##interseção elementos que se repetem
conjunto_intersecao = conjunto.intersection(conjunto2)
print('A INTERCEÇÃO É == {}'.format(conjunto_intersecao))

##DIFERENÇA DE CONJUTOS
## mostra os elementos que só tem no primeiro parametro
conjunto_diferenca = conjunto.difference(conjunto2)
print('CONJUNTO DIFERENÇA == {}' .format(conjunto_diferenca))

##DIFERENÇA SIMETRICA
## tudo que tem nos dois
conjunto_difSimetrica = conjunto.symmetric_difference(conjunto2)
print('\nCONJUNTO DIFERENÇA SIMETRICA == {}' .format(conjunto_difSimetrica))

##PERTINENCIA
##SUBCONJUNTO -
conj_a = {1,2,3}
conj_b = {1,2,3,4,5}

print('\n CONJUNTO A {}'.format(conj_a))
print(' CONJUNTO B {}'.format(conj_b))

conj_subConj = conj_a.issubset(conj_b)
print('\n O CONJUNTO A É UM SUBSET DO B ? = {}'.format(conj_subConj))

conj_subConj = conj_b.issubset(conj_a)
print('\n O CONJUNTO B É UM SUBSET DO A ? = {}'.format(conj_subConj))
print('POIS FALTA OS NUMEROS 4 e 5 no A , para que ele seja um subconj')


##SUPERSET
print('\nCONJUNTO B É UM SUPERSET DO CONJUNTO A? ')
conj_superSet = conj_b.issuperset(conj_a)
print (conj_superSet)
print('POIS ELE ENGLOBA TODOS OS VALORES DO CONJUNTO A')


##como converter uma lista para cojunto
## exemplo de estarmo trabalhando com uma lista e desejamos retirar a duplicidade da mesma

print('\nRETIRANDO DUPLICIDADE DE LISTA , COONVERTENDO PARA CONJUTO')
lista = ['dog','dog','cat','gato','eleph']
print('\nIMPRIMINDO LISTA {}'.format(lista))
conjunto_animais = set (lista)
print ('\ndepois da conversao / IMPRIMINDO CONJUNTOS {}'.format(conjunto_animais))

##CONVERTER DE VOLTA PARA LISTAS
print('\nCONVERTENDO DE VOLTA PARA LISTAS')
lista_animais =  list(conjunto_animais)
print(conjunto_animais)







