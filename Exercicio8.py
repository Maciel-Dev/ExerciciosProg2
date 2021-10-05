def f_fibo(seq):
    #Ciração da lista
    lista = [0]

    #Loop
    for i in range(seq):
        if i == 0:
            #Adiciona primeiro termo
            lista.append(1)

        #Adiciona o restante dos termos
        else:
            termo = lista[i]
            termoAnt = lista[i-1]

            lista.append(termo + termoAnt)
        

    return lista[:seq] #Retorna minha lista

def main():

    #Declaração de Variáveis
    inputUsuario = int(input())

    #Chama função

    seq = f_fibo(inputUsuario)

    print(seq) #Output



if __name__ == "__main__":
    main()