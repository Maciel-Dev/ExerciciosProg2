def fRetornaLista(numeros):
    #Retorna apenas numeros pares
    #Loop
    lista = []
    for i in range(numeros + 1):
        if i%2 == 0:
            lista.insert(0, i)


    #Retorno
    return lista

def main():

    inputUsuario = int(input())


    listaRetorno = fRetornaLista(inputUsuario)
    print(listaRetorno)



if __name__ == "__main__":
    main()
