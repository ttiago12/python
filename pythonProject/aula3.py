#verificando se um numero é par// simbolo = recebe valor // simbolo == compara valor
a = int(input('Entre com um valor: '))
resto = a % 2
if resto == 0:
    print ('O Numero é par')
else:
    print('O Numero é impar')

# #orientado a identação
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor : '))
# c = int (input ('Terceiro valor: '))
#
# #if: elif:
# if a > b and a > c:
#     print ('o maior numero é {}'.format(a))
# elif b > a and b > c:
#     print('O maior numero é {}'.format(b))
# else:
#     print ('o maior numero é {}'.format(c))
# print ('final do programa')