import numpy

def fitness(x,ff,n):
    cost=0
    for i in range(n):
        for j in range(n):
            cost=cost+ff[i,j]*(1.7+3.4*numpy.sqrt( (i-x[0])**2+(j-x[1])**2 ))
    return cost



def generare(ff,dim):
    frecventa=numpy.genfromtxt(ff)
    n=len(frecventa)
    pop=[]
    for i in range(dim):
        x=numpy.random.randint(0,n,2, dtype="int")
        val=fitness(x, frecventa,n)
        x=list(x)
        x=x+[val]
        pop=pop+[x]
    return numpy.asarray(pop)

