def listaCalc(numeroAlunos):
    lista = []
    alunosAc = 0

    for i in range(numeroAlunos):
        nota = float(input())
        lista.append(nota)
        if nota > 60:
            alunosAc += 1

    totalNotas = sum(lista)
    media = totalNotas/numeroAlunos

    return media, alunosAc




def main():

    numeroAlunos = int(input())
    retorno = listaCalc(numeroAlunos)

    print(f"A média da turma é de {retorno[0]}")
    print(f"{retorno[1]} alunos acima de 60")


    

if __name__ == "__main__":
    main()