import numpy

"0->cartonas alb" \
"1->cartonas colorat"
"Intre 2 cartonase colorate trb sa fie cel putin 1 cartonas alb"
"Numarul cartonaselor colorate este mai mare decat numarul cartonaselor albe"


def fitness(x):
    n=len(x)
    contor=0
    cartonaseAlbe=0
    cartonaseColorate=0
    for i in range(n-2):
        if x[i]==1 and x[i+1]==0 and x[i+2]==1:
            contor+=1
    for i in range(n):
        if x[i]==0:
            cartonaseAlbe+=1
        else:
            cartonaseColorate+=1
    if cartonaseColorate<cartonaseAlbe:
        return (contor-cartonaseAlbe)
    else:
        return contor


def generare(dim,nrCartonase):
    pop=numpy.zeros([dim,nrCartonase+1])
    for i in range(dim):
        x=numpy.random.randint(0,2,nrCartonase)
        val=fitness(x)
        x=list(x)
        pop[i,:nrCartonase]=x.copy()
        pop[i,-1]=val
    return numpy.asarray(pop)

