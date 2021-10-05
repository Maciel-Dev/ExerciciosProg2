def mult(k, n):
    lista = []

    for i in range(k+1):
        lista.append(n*i)

    return lista[1:]


def main():

    #Input Usuário
    k = int(input())
    n = int(input())

    resultado = mult(k, n)

    print(resultado)


if __name__ == "__main__":
    main()