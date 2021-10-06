def main():

    n = int(input())

    lista1 = []
    lista2 = []

    for i in range(n):
        l1 = int(input())
        lista1.append(l1)
        l2 = int(input())
        lista2.append(l2)

    contador = 0
    igual = 0

    while contador != n:
        if lista1[contador] == lista2[contador]:
            igual += 1

        contador += 1

    print(f'{igual} termos iguais!')

if __name__ == "__main__":
    main()