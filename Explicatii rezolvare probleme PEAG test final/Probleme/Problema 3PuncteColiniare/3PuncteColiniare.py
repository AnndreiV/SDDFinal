"Gasiti 3 puncte coliniare din spatiul solutiilor [-10;10] NUMERE INTREGI"
"6 gene: x=[x1,y1,x2,y2,x3,y3]"
"           0  1  2  3  4  5   "
"Fitness: (y3-y1)/(y2-y1)=(x3-x1)/(x2-x1) =>daca e true return 1 else return 0"

import numpy
def fitness(x):

    if(x[0]==x[2]==x[4] or x[1]==x[3]==x[5]):
        return 1

    if(x[0]==x[2] or x[1]==x[3]):
        return 0
    s=(x[5]-x[1])/(x[3]-x[1])
    d=(x[4]-x[0])/(x[2]-x[0])

    if s==d:
        return 1
    else:
        return 0

def gen(dim):
    pop=[]
    for i in range(dim):
        x=numpy.random.randint(-10,11,6)
        val=fitness(x)
        x=list(x)
        x=x+[val]
        pop=pop+[x]
    return numpy.asarray(pop)


