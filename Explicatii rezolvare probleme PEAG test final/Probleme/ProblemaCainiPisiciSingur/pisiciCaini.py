import numpy
"Aranjați n câini și m (m>1) pisici în cerc astfel încât între 2 câini" \
" (aranjați consecutiv) fie să nu se afle nicio pisică, fie să existe cel puțin două."

"Avem o permutare :[0, 1, 2, 3, 4, 5, 6, 7, 8] unde valorile de la 0 pana la 5 sunt caini iar valorile de la 6 la 8 sunt pisici" \
"Caini: 0,1,2,3,4,5" \
"Pisici: 6,7,8" \
"" \
"Avem un contor initializat cu 0 pe care il incrementam de fiecare data cand intre 2 caini nu gasim o pisica."

def fitness(x):
    contor=0
    n=len(x)-1

    for i in range(n):
        if x[i]<6 and x[i+1]<6:
            contor+=1
    if x[0]<6 and x[n]<6:
        contor+=1
    return contor

def generare(dim):
    pop=[]
    for i in range(dim):
        x=numpy.random.permutation(9)
        val=fitness(x)
        x=list(x)
        x=x+[val]
        pop=pop+[x]
    return numpy.asarray(pop)


