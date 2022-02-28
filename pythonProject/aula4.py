## imprimir o 100 primeiro numero
## range de 100 pega de 0 ate 99 , também é posivel determinar
##em qual numero começar (nINCIAL,nFINAL)
# for x in range(1,100):
#     print(x)
## verificar numeros primos
# a = int (input('Entre com um numero: '))
# div = 0
# for x in range (1,a+1):
#     resto = a % x
#     if resto == 0:
#         div = div + 1 ##outra forma também é : div += 1
#
# if div == 2 :
#     print ('numero {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))




##verificando numeros primos dentro de um periodo
##utilizando o for e colocando o codigo anterior dentro do for
##percorre de 0 ao numero A e imprime os primos
a = int (input('Entre com um valor: '))
for num in range(a):
    div = 0
    for x in range(1,num+1):
        resto = num % x
        if resto == 0:
            div = div + 1  ##outra forma também é : div += 1
    if div == 2:
        print(num)

