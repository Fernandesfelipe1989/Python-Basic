lista =[1, 0]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[1]



except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print("Erro desconhecido. Erro: {} ".format(ex))
else:
    print('Deu bom')
finally:
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()
