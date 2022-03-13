class File:


    def criar(nomeArquivo):
        nomeArquivo = input('NOME DO ARQUIVO= ')
        arquivo = open(nomeArquivo,'x')

file = File()

file.criar()