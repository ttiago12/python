##personalizando excecao

##CRIO UMA CLASSE QUE HERDA DE EXCEÇAO
class Error(Exception):
    pass

class InputError(Error):
    def __int__(self, message):
        self.message = message

##EXECUTA PARA SEMPRE ATE DIGITAR UM NUMERO
while True:
    try:
        x = int(input('ENTRE COOM UMA NOTA DE 0 A 10 \n ='))
        print(x)

        ##aonde acontece a personalizacao
        if x > 10:
            ##forcandouma excecao
            raise InputError('Nota nao pode ser maior que 10')
        elif x < 0:
            ##forcando um excecao
            raise InputError('Nota não pode menor que 0  ')
        ## se o obtiver sucesso sai do while
        break
    except ValueError:
        print('Valor invalido . DIGITE SOMENTE NUMEROS')
    except InputError as ex:
        print(ex)