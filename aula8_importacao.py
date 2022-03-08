#formar de importar modulos
from click._compat import term_len

from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
##CASO ALGUEM CHAMAR DE FORA ESTAS AÇÕES NÃO SERÃO EXECUTADAS
if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)


##fazendo simplesmente isso e não sem a utilização do main
##tudo seria retornado
calculadora = Calculadora(8,12)
print('SOMA')
print(calculadora.soma())