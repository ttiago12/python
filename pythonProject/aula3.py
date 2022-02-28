# ## media bimestral e valida se nota foi digitada corretamente
# a = int (input('Primeiro bimestre: '))
# b = int (input('Segundo bimestre:'))
# c = int (input('Terceiro bimestre:'))
# d = int (input('Quarto bimestre: '))
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10  and  c <= 10 and d <= 10:
#     print ('Media:  {}'.format(media))
# else:
#     print('FOI INFORMADA UMA NOTA INCORRETA')

## media bimestral e valida se nota foi digitada corretamente
##validando no momento da leitura do valor
a = int (input('Primeiro bimestre: '))
## se o numero for maior que 10 ele requisita novamente o valor a seguir
if a > 10:
    a = int(input('Você digitou errado.Digite novamente// Primeiro bimestre: '))
b = int (input('Segundo bimestre:'))
if b > 10:
    b = int(input('Você digitou errado.Digite novamente// Primeiro bimestre: '))
c = int (input('Terceiro bimestre:'))
if c > 10:
    c = int(input('Você digitou errado.Digite novamente// Primeiro bimestre: '))
d = int (input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado.Digite novamente// Primeiro bimestre: '))
media = (a + b + c + d) / 4
if a <= 10 and b <= 10  and  c <= 10 and d <= 10:
    print ('Media:  {}'.format(media))
else:
    print('FOI INFORMADA UMA NOTA INCORRETA')




#verificando se um numero é par// simbolo = recebe valor // simbolo == compara valor
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print ('foi digitado um numero par')
#
# else:
#     print('Nenhum numero par foi digitado')


# if resto == 0:
#     print ('O Numero é par')
# else:
#     print('O Numero é impar')

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