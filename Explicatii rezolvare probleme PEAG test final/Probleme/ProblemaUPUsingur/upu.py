import numpy
frecvente=numpy.genfromtxt("frecvente.txt")
n=len(frecvente)
def fitness(x):
    total=0
    for i in range(n):
        for j in range(n):
            total+= frecvente[i, j] * (1.7 + 3.4 * numpy.sqrt((i - x[0]) ** 2 + (j - x[1]) ** 2))
    return 1/1+total


def generare(fisier,dim):
    pop=[]
    for i in range(dim):
        x=numpy.random.randint(0,n,2)
        val=fitness(x)
        x=list(x)
        x=x+[val]
        pop=pop+[x]
    return numpy.asarray(pop)
