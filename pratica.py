class File:
    def criar(nomeArquivo):
        nomeArquivo = input('NOME DO ARQUIVO= ')
        arquivo = open(nomeArquivo,'x')
        arquivo.close
    def escrever(texto):
        nomeArquivo = input('NOME DO ARQUIVO= ')

        arquivo = open(nomeArquivo,'w')


file = File()

file.criar()

file.escrever(input())