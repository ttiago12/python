## so escreve usa o w
##atualizar usa o a
import shutil

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
    ##deifine aluno_nota = ao que esta dentro do arquivo le o arquivo
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    ##utilizando o o split transformar em lista e separar em 'valor'
    ##sempre que ele achar algo que foi definido no split('')
    ##no caso inicialmente utilizamendo a quebra de linha como parametro

    #print('\nAGORA COM O SPLIT pela quebra de linhna')
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    #percorrer o arquivo
    #novo split pela virgula
    #print('///////////////////////\n novo split pela virgula')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        #print(listas_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print (aluno)
        print(lista_notas)
        media = lambda notas: sum([int (i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
    print('/////////')

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/home/tux/Documentos/GitHub/copiou.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,'/home/tux/Documentos/GitHub/'
                             '')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    #escrever_arquivo('Primeira linha.\n')
    # aluno = 'Hugo,8,10,7,9'
    # atualizar_arquivo('notas.txt', aluno)
    ##ler_arquivo('teste.txt')