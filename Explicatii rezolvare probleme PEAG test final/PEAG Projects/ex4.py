import numpy as np

COSTURI = np.genfromtxt('COSTURI.txt')
CERERE = np.genfromtxt('CERERE.txt')
OFERTA = np.genfromtxt('OFERTA.txt')

m = len(OFERTA)
n = len(CERERE)

def fitness(individ):
    x = np.zeros((m,n))
    for i in individ:
        lin, col = np.unravel_index(i, (m,n))
        x[lin][col] = 1
    costTotal=0
    for i in range(m):
        for j in range(n):
            costTotal+=COSTURI[i][j]*x[i][j]
    return 1000/costTotal

def gen_pop(dim):
    pop = []

    for i in range(dim):
        x=np.random.permutation(m*n)
        val=fitness(x)
        x=list(x)
        x=x+[val]
        pop=pop+[x]
    return np.asarray(pop)


'''if __name__ == '__main__':
    NR_INDIVIZI = 100
    NMAX = 500
    PC = 0.8
    PM = 0.1
    pop = gen_pop(NR_INDIVIZI)
    print('Populatia initiala:')
    for line in sorted(pop, key=lambda x: x[-1]):
        print(line)
    i=1
    gata = False
    while i<=NMAX and not gata:
        spop = SUS_cu_FPS_standard(pop, NR_INDIVIZI)
        copii = incrucisare(spop, NR_INDIVIZI, PC)
        copii_m = mutatie(copii, PM)
        pop = elitism(pop, copii_m, NR_INDIVIZI)
        if len(set(pop[:,-1])) == 1:
            gata = True
        i += 1
    print('Populatia finala:')
    for line in sorted(pop, key=lambda x: x[-1]):
        print(line)'''