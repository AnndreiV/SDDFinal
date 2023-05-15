ld = [[9, 1], [4, 4], [3, 1], [3, 5], [7, 8], [2, 4]]
"        0       1       2       3       4       5"
"[2, 4][7,8][4 4][3 5][9 1][3 1]"
import numpy
def fitness(x):
    contor = 0
    global ld
    lista = ld
    n = len(lista)
    for i in range(n - 1):
        if lista[x[i]][1] % 2 == lista[x[i+1]][0]%2:
            contor += 1
    return contor

def generare(dim):
    pop = []
    global ld
    n = len(ld)
    for i in range(dim):
        x = numpy.random.permutation(n)
        val = fitness(x)
        x = list(x)
        x = x + [val]
        pop = pop + [x]
    return numpy.asarray(pop)
