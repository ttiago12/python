#forma de importar modulos
from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras
##CASO ALGUEM CHAMAR DE FORA ESTAS AÇÕES NÃO SERÃO EXECUTADAS
if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    lista = ['vaca','camelo','iguana']
    print('TOTAL LETRAS')
    print(contador_letras(lista))

##fazendo simplesmente isso e não sem a utilização do main
##tudo seria retornado
calculadora = Calculadora(8,12)
print('SOMA')
print(calculadora.soma())