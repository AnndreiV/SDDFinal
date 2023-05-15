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

import numpy

conflicte=numpy.genfromtxt("conflicte.txt")
n=len(conflicte)

def fitness(x):
    contor=0
    for i in range(n-1):
        if conflicte[x[i]][x[i+1]]==1:
            contor+=1
    if conflicte[x[0]][x[-1]]==1:
        contor+=1
    return 1/(1+contor)
    'functie de maxim, daca e 1, inseamna ca am gasit o solutie'

def generare(dim):
    pop=[]
    for i in range(n):
        x=numpy.random.permutation(n)
        val=fitness(x)
        x=list(x)
        x=x+[val]
        pop=pop+[x]
    return numpy.asarray(pop)