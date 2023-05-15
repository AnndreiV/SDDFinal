import numpy

#functia obiectiv
def fAvioane(x, autonomie):
    val=numpy.dot(x,autonomie)
    nr_av=numpy.sum(x)
    if(nr_av):
        val=val/nr_av
    return val

#Verificare admisibil

def admisibil(x, vizibilitate, cost, costmax, vmin):
    vmed=numpy.dot(x,vizibilitate)
    cost=numpy.dot(x,cost)
    nr_av=sum(x)
    if(nr_av):
        vmed=vmed/nr_av
    return cost <=costmax and vmed>vmin

#Generare populatie initiala

def gen(c,v,a,dim,costmax,vmin):
    cost=numpy.genfromtxt(c)
    vizibilitate=numpy.genfromtxt(v)
    autonomie=numpy.genfromtxt(a)
    n=len(cost)
    variante=[int(costmax/cost[i]) for i in range(n)]
    pop=numpy.zeros([dim,n], dtype="int")
    qual=numpy.zeros(dim)
    i=0
    while i<dim:
        x=numpy.zeros(n)
        for k in range(n):
            x[k]=numpy.random.randint(0,variante[k]+1)
            if(admisibil(x,vizibilitate,cost, costmax,vmin)):
                pop[i]=x.copy()
                qual[i]=fAvioane(pop[i],autonomie)
                i+=1
    return pop,qual


