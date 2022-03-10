## so escreve usa o w
##atualizar usa o a

def escrever_arquivo(texto):
##também consegue determinar um diretorio
    diretorio = '/home/tux/Documentos/GitHub/teste.txt'
    arquivo = open(diretorio, 'w')
    ## arquivo = open ('arquivo.txt', w) cria dentro da pasta deste arquivo
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open ('teste.txt','a')
    arquivo.write(texto)
    arquivo.close()

## R realiza a leitura
def ler_arquivo(nome_arquivo):
        arquivo = open (nome_arquivo, 'r')
        texto = arquivo.read()
        print (texto)
if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    ##atualizar_arquivo('3° Linha. \n')
    ##ler_arquivo('teste.txt')