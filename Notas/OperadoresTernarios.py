esta_chovendo = False

print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])

print('Hoje estou com as roupas ' + ('molhadsas.' if esta_chovendo else 'secas.'))

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_b is lista_c)
print(lista_a is not lista_c)

dir()
