# Operador de membro

lista = [1, 2, 3, 'Ana', 'Maria']
print(2 in lista)
print('Ana' not in lista)

# Operadores de identidade

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_b is lista_c)
print(lista_a is not lista_c)