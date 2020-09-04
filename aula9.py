import shutil

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    return texto


def media_notas(nome_arquivo):
    # print(ler_arquivo(nome_arquivo))
    aluno_nota = ler_arquivo(nome_arquivo).split('\n')
    lista_nota = []
    lista_media =[]
    nota = []
    for x in aluno_nota:
        lista_nota = x.split(',')
        aluno= lista_nota.pop(0)
        media = lambda notas: sum([int(i) for i in notas])/(len(notas))
        lista_media.append({aluno:media(lista_nota)})
    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, "D:\Documentos\Felipe")
    return 'notas.txt'

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, "D:\Documentos\Felipe\Python")

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    move_arquivo(copia_arquivo('notas.txt'))

    print(lista_media)
    #escrever_arquivo("Primeira linha.\n")
    # aluno ='\nGalleano,7,5,5,3'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')