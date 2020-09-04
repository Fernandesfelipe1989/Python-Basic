# conjunto ={1, 2, 3, 4, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)

conjunto ={1, 2, 3, 4, 5}
conjunto2 ={5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção :{}'.format(conjunto_interseccao))
print('Diferença entre 1 e 2: {}'.format(conjunto.difference(conjunto2)))
print('Diferença entre 2 e 1: {}'.format( conjunto2.difference(conjunto)))
print('Diferença simétrica: {}'.format(conjunto.symmetric_difference(conjunto2)))

conjunto_a ={1, 2, 3}
conjunto_b ={1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)