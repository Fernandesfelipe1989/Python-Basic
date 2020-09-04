from aula7_televisao import Televisao
from aula8_contador_letras import contador_letras, test
if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligado)
    televisao.power()
    print(televisao.ligado)
    print(test())
    lista = ['cachorro', 'gato', 'elefante']
    print("Total de letras por palavra da lista {}".format(contador_letras(lista)))