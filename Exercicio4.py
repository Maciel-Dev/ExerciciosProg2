def main():
    lista = []

    for i in range(5): #Possibilidade de definição do usuário
        inputUser = input("Digite um carcter ou numero: ")
        lista.append(inputUser)

    resUser = input("Digite o caracter a ser buscado: ")

    while resUser != "/":
        ocNum = 0

        for element in lista:
            if element == resUser:
                ocNum += 1

        print(f"A quantidade de caracter '{resUser}' na lista é igual a {ocNum}")

        resUser = input("Digite o caracter a ser buscado: ")

            





if __name__ == "__main__":
    main()