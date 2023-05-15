import numpy as np

COSTURI = [1000, 800, 1500]
CREDITE = [5, 3, 8]
ORE_STUDIU = [80,40,100]

def fitness(x):
    return (x[0]*CREDITE[0]+x[1]*CREDITE[1]+x[2]*CREDITE[2])/np.sum(x)

def gen_pop(dim):
    pop = []
    for i in range(dim):
        individ = [np.random.randint(low=0, high=51), np.random.randint(low=0, high=84), np.random.randint(low=0, high=100)]
        gata = False
        while not gata:
            if COSTURI[0] * individ[0] + COSTURI[1] * individ[1] + COSTURI[2] * individ[2] > 5000:
                individ = [np.random.randint(low=0, high=51), np.random.randint(low=0, high=84), np.random.randint(low=0, high=100)]
                continue
            if (ORE_STUDIU[0] * individ[0] + ORE_STUDIU[1] * individ[1] + ORE_STUDIU[2] * individ[2]) < 40:
                individ = [np.random.randint(low=0, high=51), np.random.randint(low=0, high=84), np.random.randint(low=0, high=100)]
                continue
            gata = True
        individ += [fitness(individ)]
        pop.append(individ)
    return pop

if __name__ == '__main__':
    print('Populatia initiala:')
    NMAX = 400
    NR_INDIVIZI = 100
    PC = 0.8
    PM = 0.1
    pop = gen_pop(NR_INDIVIZI)
    for line in sorted(pop, key=lambda x: x[-1]):
        print(line)
    i = 1
    gata = False
    max_qual = max(pop[:, -1])
    nrm = 1
    while i<=NMAX and not gata:
        spop = ruleta_fps_sigma_scalare(pop, NR_INDIVIZI)
        copii = incrucisare(spop, NR_INDIVIZI, PC)
        copii_m = mutatie(copii, PM)
        pop = elitism(pop, copii_m, NR_INDIVIZI)
        max_qual_nou = max(pop[:, -1])
        if max_qual_nou == max_qual:
            nrm += 1
        else:
            nrm = 1
            max_qual = max_qual_nou
        if nrm == NMAX//4:
            gata = True
        i += 1
    print('Populatia finala:')
    for line in sorted(pop, key=lambda x: x[-1]):
        print(line)
