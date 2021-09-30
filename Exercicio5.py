def main():

    listaTeste = [1,3,4,534,62344,8534,25783902,1,613721,8,10,12]

    maiorNum = 0

    #Função
    for i in listaTeste:
        if i > maiorNum:
            maiorNum = i
        
    print(maiorNum)

    #Utilizando Max
    print(max(listaTeste))



if __name__ == "__main__":
    main()