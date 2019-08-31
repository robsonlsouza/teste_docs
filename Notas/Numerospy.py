from decimal import Decimal, getcontext

getcontext().prec = 4
print(Decimal(1.1) / Decimal(2.2))

dir(Decimal)

getcontext.prec = 7
print(1.1 + 2.2)
