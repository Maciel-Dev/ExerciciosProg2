import random

def reverseL(lista):
    listaInvertida = lista[::-1]

    return listaInvertida

def main():

    #Criação da lista
    lista = []

    #Loop
    for i in range(5):
        #Acréscimo de valores aleatórios
        numeroA = random.randint(0,100)
        lista.append(numeroA)

    #Chama Função
    invertLista = reverseL(lista)

    print(invertLista)

if __name__ == "__main__":
    main()
