import numpy as np

def calcul_lungime(x,y,z,t):
    return np.sqrt((x-y)**2+(z-t)**2)

def fitness(x):
    distante = [calcul_lungime(x[0],x[1],x[2],x[3]), calcul_lungime(x[0],x[1],x[4],x[5]), calcul_lungime(x[2],x[3],x[4],x[5])] # AB, AC, BC
    diferente = [distante[0]-distante[1]-distante[2],distante[1]-distante[0]-distante[2], distante[2]-distante[0]-distante[1]]
    formule = [1/(diferente[i]+1) for i in range(3)]
    return np.max(formule)

def gen_pop(dim):
    pop = []
    for i in range(dim):
        individ = np.random.randint(0,100,6).tolist()
        individ += [fitness(individ)]
        pop.append(individ)
    return pop

if __name__ == '__main__':
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
        spop = SUS_cu_FPS_scalare(pop, NR_INDIVIZI)
        copii = incrucisare_uniforma(spop, NR_INDIVIZI, PC)
        copii_m = resetare_aleatorie(copii, PM)
        pop = elitism(pop, copii_m, NR_INDIVIZI)
        if len(set(pop[:,-1])) == 1:
            gata = True
        i += 1
        max_qual = np.max(pop[:,-1])
        if abs(max_qual) < 0.00001:
            gata = True
    print('Populatia finala:')
    for line in sorted(pop, key=lambda x: x[-1]):
        print(line)
