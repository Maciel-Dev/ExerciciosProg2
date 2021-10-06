def calcTemp(dias):

    lista=[]

    for i in range(dias):
        temp = float(input())
        lista.append(temp)

    somaTemp = sum(lista)
    media = somaTemp/dias

    tempAbaixo = 0

    for element in lista:
        if element < media:
            tempAbaixo += 1

    return tempAbaixo


def main():

    n = int(input())
    nDias = calcTemp(n)

    print(f"Número de dias que a temperatura ficou abaixo da média é igual a {nDias}")

if __name__ == "__main__":
    main()