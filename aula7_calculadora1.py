# ## metodoss
# ##todo codigo que eu for utilizar ele muitas vezes , posso transforma-lo em metodo
# def soma (a,b):
#     return a + b
# def subtr (a,b):
#     return a - b
# def mult (a,b):
#     return a * b
# def div (a,b):
#     return a / b
#
# print(soma(1,2))
# print(soma(5,9))
# print(subtr(14,9))
# print(mult(1,2))
# print(div(14,2))

##CLASSE
class Calculadora:
    ##criar um valor de inicialização da classe criando um metodo chamado init
    def __init__(self,num1,num2):
        self.valor_a = num1
        self.valor_b = num2

    ## isso significa que sempre que eu for instanciar a classe calculadora
    ##ele obrigatoriamente vai passar pelo metodo init
    def soma (self):
        return self.valor_a + self.valor_b
    def subtr (self):
        return self.valor_a - self.valor_b
    def mult (self):
        return self.valor_a * self.valor_b
    def div (self):
        return self.valor_a / self.valor_b

## instanciando uma classe
if __name__ == '__main__':

    calculadora = Calculadora(10,2)
    print('IMPRIMINDO O VALOR {}=Valor_a'.format(calculadora.valor_a))
    print('IMPRIMINDO O VALOR {}=Valor_b'.format(calculadora.valor_b))
    print('IMPRIMINDO O VALOR {}=ValorSoma'.format(calculadora.soma()))
    print('IMPRIMINDO O VALOR {}=ValorSubtracao'.format(calculadora.subtr()))
    print('IMPRIMINDO O VALOR {}=ValorDivisao'.format(calculadora.div()))
    print('IMPRIMINDO O VALOR {}=ValorMuliplicacao'.format(calculadora.mult()))