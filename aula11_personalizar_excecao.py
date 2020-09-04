class Error(Exception):
    pass
class InputError(Error):
    def __init__(self, message):
        self.message = message
    pass

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        if x > 10:
            raise InputError('Erro: Nota não pode ser maior do que 10')
        elif x < 0:
            raise InputError('Erro: Nota não pode ser menor do que 0')

        break
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números")
    except InputError as ex:
        print(ex)