import numpy


def fitness(matrice, x):
    n=len(matrice)
    contor=0
    for i in range(n-1):
        if numpy.sum(matrice[x[i]])%2==numpy.sum(matrice[x[i+1]])%2:
            contor+=1
    return contor


def generare(dim):
    matrice=numpy.zeros([dim, 5],dtype="int")
    n=len(matrice)
    for i in range(n):
        matrice[i,:5]=numpy.random.randint(0,2,5)

    "Mai sus doar ne-am generat matricea, o puteam face si intr-un fisier txt"
    pop=[]
    for j in range(n):
        x=numpy.random.permutation(dim)
        val=fitness(matrice,x)
        x=list(x)
        x=x+[val]
        pop=pop+[x]
    return numpy.asarray(pop), numpy.asarray(matrice)
