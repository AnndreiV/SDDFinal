"""CERINTA: Cele n orașe stat din Grecia antică se luptă între ele pentru dominație, dar în fața unei amenințări externe
hotărăsc să se unească. Pentru a stabili planul de apărare, delegații orașelor urmează să se întîlnească, fiecare
oraș desemnîndu-și un singur reprezentant. Cunoscînd rivalitățile istorice dintre orașe, folosiți un algoritm
genetic pentru a găsi o modalitate de așezare a delegaților la masa (rotundă) tratativelor astfel încît delegații
din orașe rivale să nu fie vecini (se presupune că acest lucru este posibil).
Harta orașelor stat între care există animozități este exprimată printr-o matricea pătratică de ordin n, numită
CONFLICT:
𝐶𝑂𝑁𝐹𝐿𝐼𝐶𝑇(𝑖, 𝑗) = {
0, 𝑑𝑎𝑐ă 𝑖 ș𝑖 𝑗 𝑛𝑢 𝑠𝑒 𝑎𝑓𝑙ă î𝑛 𝑠𝑡𝑎𝑟𝑒 𝑑𝑒 𝑐𝑜𝑛𝑓𝑙𝑖𝑐𝑡 𝑠𝑎𝑢 𝑖 = 𝑗
1, 𝑑𝑎𝑐ă 𝑜𝑟𝑎ș𝑢𝑙 𝑠𝑡𝑎𝑡 𝑖 𝑒𝑠𝑡𝑒 î𝑛 𝑐𝑜𝑛𝑓𝑙𝑖𝑐𝑡 𝑐𝑢 𝑜𝑟𝑎ș𝑢𝑙 𝑠𝑡𝑎𝑡 𝑗"""
import numpy as np

CONFLICTE = np.genfromtxt('CONFLICT.txt', dtype=int)


# Individul este o permutare a numerelor de la 0 la len(CONFLICTE)-1 inclusiv (reprezentand delegatii oraselor)
# Functia fitness va fi mai mare cu cat numarul de conflicte dintre delegati este mai mic
# ex individ = [0, 5, 2, 3, 6, 9, 8, 7, 4, 1]
def fitness(individ):
    """Functia de fitness"""
    fit = 0
    for i in range(len(individ) - 1):
        for j in range(i + 1, len(individ)):
            if CONFLICTE[individ[i]][individ[j]] == 1:
                fit += 1
    if CONFLICTE[individ[0]][individ[-1]] == 1:
        fit += 1
    return 1 / (fit + 1)


def gen_pop(dim):
    """Generarea unei populatii de dimensiune dim"""
    pop = []
    for i in range(dim):
        individ = np.random.permutation(len(CONFLICTE))
        pop.append(list(individ) + [fitness(individ)])
    return np.asarray(pop)


'''if __name__ == '__main__':
    NR_ITERATII = 500
    NR_INDIVIZI = 100
    i = 1
    gata = False
    pop = gen_pop(NR_INDIVIZI)
    max_qual = max(pop[:, -1])
    nrm = 1
    while i<=500 and not gata:
        # selectia parintilor prin metoda ruletei
        spop = ruleta(pop, NR_INDIVIZI, len(CONFLICTE))
        # recombinarea parintilor
        copii = OCX(spop, NR_INDIVIZI, len(CONFLICTE), prob_rec=0.7)
        # mutatia copiilor
        copii_m = interschimbare(copii, len(CONFLICTE), prob_mut=0.1)
        # selectia supravietuitorilor
        pop = elitism(pop, copii_m, NR_INDIVIZI).copy()
        minim = min(pop[:, -1])
        maxim = max(pop[:, -1])
        if maxim == max_qual:
            nrm += 1
        else:
            max_qual = maxim
            nrm = 1
        if maxim == minim or nrm == int(NR_ITERATII/10):
            gata = True
        i += 1
        max_qual = maxim
    print("Solutia optima este: ", pop[np.argmax(pop[:, -1])])'''