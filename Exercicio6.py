import random

def maiorF(lista):
    maiorNumero = lista[0] #condição de comparação
    indice = 0

    contador = 0

    while contador != len(lista):
        if lista[contador] > maiorNumero:
            maiorNumero = lista[contador]
            indice = contador

        contador += 1

    return indice, maiorNumero

        

def main():

    #Criação da lista
    lista = []

    #Loop
    for i in range(5):
        #Acréscimo de valores aleatórios
        numeroA = random.randint(0,100)
        lista.append(numeroA)

    #Chama Função
    indiceFunc = maiorF(lista)

    #Saída de dados
    print(f'O índice do maior número é {indiceFunc[0]}')
    print(f"O maior número é igual a {indiceFunc[1]}")

if __name__ == "__main__":
    main()
