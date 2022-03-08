a = 10
b = 5
soma = a +  b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#imprime o tipo de dado que a variavel retorna
print (type(soma))

#converte inteiro para uma String
print('soma = ' + str(soma))
print('subtração = '+ str(subtracao))
print('multiplicao = ' + str(multiplicacao))
print('DIVISAO = '+ str (divisao))
print('TIPO DA VARIAVEL DIVISAO ')
print(type(divisao))

#transforma em numero intero
print( int(divisao))
print(resto)

##CONCATENANDO VARIAVEIS

x = '1'
## o x era uma string , na linha abaixo para realizar a soma foi passado para inteiro
soma2 = int(x) + 1
print ('SOMA2= ' + str(soma2))

##usando o format , contatena idependente do tipo
print ('SOMA-FORMAT = {}. subtracao-FORMAT = {} ' .format(soma,subtracao))

#usando alias no format dentro de {}
print("\nUTILIZANDO ALIAS")
print ('Soma : = {soma} '
       '\n Subtração = {subtracao} '
       '\n Multiplicao = {multiplicacao} '
       '\n Divisao = {divisao} '
       '\n Resto : {resto}'.format(soma = soma,
                subtracao = subtracao,
                resto = resto,
                divisao = divisao,
                multiplicacao = multiplicacao))

#INTERAGIR COM USUARIO
c = input('primeiro valor :')
d = input ('segundo valor :')
# converter o valor recebido para inteiro  // d = int (input ('segundo valor :'))



