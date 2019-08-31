import sys
from math import pi
import errno


def help():
    print("É mecessário informar a área do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print("O raio deve ser um número.")
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print(area)
