class Televisao:
    def __init__(self):
        self.ligada = False ##começando desligada
        self.canal = 12

    ##metodo para ligar e desligar a TV
    def power(self):
        if self.ligada: ## é o mesmo que a self.ligada é verdadeira?
            self.ligada = False ##desliga a tv
        else: ## se não , liga  a tv
            self.ligada = True ##liga a tv

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
        else:
            print('TV NAO ESTA LIGADA')
    def diminui_canal(self):
        if self.ligada:
            self.canal-= 1
        else:
            print('TV NAO ESTÁ LIGADA')
##instanciamos a classe Televisao,
televisao = Televisao()
print('TELEVISAO ESTA LIGADAA {}'.format(televisao.ligada))
televisao.power()
print('TELEVISAO ESTA LIGADAA {}'.format(televisao.ligada))
televisao.power()
print('TELEVISAO ESTA LIGADAA {}'.format(televisao.ligada))
televisao.power()
print('CANAL DA TV {}'.format(televisao.canal))

print('\nAUMENTANDO CANAL//////')
televisao.aumenta_canal()
print('CANAL DA TV {}'.format(televisao.canal))
televisao.power()
print('\nDIMINUINDO CANAL//////')
televisao.diminui_canal()
print('CANAL DA TV {}'.format(televisao.canal))