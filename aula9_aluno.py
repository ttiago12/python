## so escreve usa o w
##atualizar usa o a

def escrever_arquivo(texto):
##também consegue determinar um diretorio
    diretorio = '/home/tux/Documentos/GitHub/teste.txt'
    arquivo = open(diretorio, 'w')
    ## arquivo = open ('arquivo.txt', w) cria dentro da pasta deste arquivo
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open (nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()

## R realiza a leitura
def ler_arquivo(nome_arquivo):
        arquivo = open (nome_arquivo, 'r')
        texto = arquivo.read()
        print (texto)
def media_notas(nome_arquivo):
    arquivo = open (nome_arquivo , 'r')
    ##le arquivo
    aluno_nota = arquivo.read()
    print(aluno_nota)
    for x in aluno_nota:
        print(x)

if __name__ == '__main__':
    media_notas('notas.txt')
    ##escrever_arquivo('Primeira linha.\n')
    ##aluno = '\nCesar ,8,10,7,9'
    ##atualizar_arquivo('notas.txt', aluno)
    ##ler_arquivo('teste.txt')