##caso eu queira continuar tendo a classe mas não quero instanciar os objetos
##retiro os parametros do init
class Calculadora:
    ##criar um valor de inicialização da classe criando um metodo chamado init
    def __init__(self):
        pass ## vazio

    ## isso significa que sempre que eu for instanciar a classe calculadora
    ##ele obrigatoriamente vai passar pelo metodo init
    def soma (self,valor_a, valor_b):
        return valor_a + valor_b
    def subtr (self,valor_a, valor_b):
        return valor_a - valor_b
    def mult (self,valor_a, valor_b):
        return valor_a * valor_b
    def div (self,valor_a, valor_b):
        return valor_a / valor_b

## neste caso nao predefinimos o valor , ele será inserido em cada print
calculadora = Calculadora()
# print('IMPRIMINDO O VALOR {}=Valor_a'.format(calculadora.valor_a))
# print('IMPRIMINDO O VALOR {}=Valor_b'.format(calculadora.valor_b))
print('IMPRIMINDO O VALOR {}=ValorSoma'.format(calculadora.soma(1,5)))
print('IMPRIMINDO O VALOR {}=ValorSubtracao'.format(calculadora.subtr(9,6)))
print('IMPRIMINDO O VALOR {}=ValorDivisao'.format(calculadora.div(18,3)))
print('IMPRIMINDO O VALOR {}=ValorMuliplicacao'.format(calculadora.mult(3,5)))