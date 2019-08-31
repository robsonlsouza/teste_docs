True or False

print(7 != 3 and 2 > 3)

print(45 == 44)

# Tabela Verdade do AND
print(True and True)
print(True and False)
print(False and False)
print(False and True and False and True)
print(True and True)

# Tabela verdade do OR

print(True or True)
print(False or False)
print(True or False)
print(False or False)

# Tabela verdade exclusivo

print(False != False)
print(False != True)
print(True != True)
print(True != False)

print("Operadores de Negação")

print(not True)
print(not False)
print(not 0)
print(not not -1)
print(not not True)


# Um pouco de realidade

saldo = 1000
salario = 4000
despesas = 20000

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas

print("____________________________________________")
print(meta)
