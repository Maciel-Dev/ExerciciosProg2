import random

def f_listas(listaOrd, listaAbs):

    ordImp = 0
    absPar = 0

    newListAbs = []
    newListOrd = []

    for i in listaOrd:
        if i % 2 != 0:
            ordImp += 1
            newListOrd.append(i)

    for j in listaAbs:
        if j % 2 == 0:
            absPar += 1
            newListAbs.append(j)

    if absPar >= ordImp:
        soma = 0
        
        for k in newListAbs:
            soma += k

        return "Abs",soma

    else:
        mult = 1
        
        for l in newListOrd:
            mult = mult*l

        return "Ord",mult




def main():

    listaOrd = []
    listaAbs = []

    for i in range(5):
        listaOrd.append(random.randint(0,100))
        listaAbs.append(random.randint(0,100))

    retornoF = f_listas(listaOrd, listaAbs)

    print(f"{listaOrd}\n")
    print(f"{listaAbs}\n")

    print(f"{retornoF}")



if __name__ == "__main__":
    main()