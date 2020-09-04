contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))
soma = lambda a, b: a+b
print(soma(5, 10))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda  a, b: a / b,
        }
print(type(calculadora))
soma = calculadora['soma']
subtracao = calculadora['subtracao']
print('A soma é: {}'.format(soma(10, 5)))
print('A substração é: {}'.format(subtracao(8, 2)))
