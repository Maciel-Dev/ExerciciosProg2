def fEmpresa(quant):
    
    matriz = []
    somaSalario = 0
    listaNomes = []

    for i in range(quant):

        nome = input("Digite o nome do funcionário: ")
        salario = float(input(f"Digite o salário do funcionário {nome}: "))

        matriz.append([nome, salario])

    for j in range(len(matriz)):
        somaSalario += matriz[j][1]

    media = somaSalario/quant

    for funcionarios in range(quant):
        if matriz[funcionarios][1] > media:
            listaNomes.append(matriz[funcionarios][1])

    return listaNomes


def main():

    n = int(input())

    nomeSalario = fEmpresa(n)

    for funcionario in nomeSalario:
        print(funcionario)

if __name__ == "__main__":
    main()