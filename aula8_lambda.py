##lambada só é eficiente para funções que de para resolver com uma
##unica linha
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro','gato','elefante']
print(contador_letras(lista_animais))

##fazendo uma calculadora
soma = lambda a, b : a + b
print(soma(12,9))

##varios lambdas em um só

calculadora = {
    'soma': lambda  a,b : a + b,
    'substracao': lambda a,b : a- b,
    'multiplicacao': lambda a,b : a * b,
    'divisao': lambda a,b : a / b,
}

##verificando o tipo de calculadora
print(type(calculadora))

##imprimindo os resultados
soma = calculadora['soma']
multiplicacao = calculadora ['multiplicacao']
print('a soma é : {}'.format(soma(10,5)))
print('a multiplicacao é :{}'.format(multiplicacao(10,2)))

