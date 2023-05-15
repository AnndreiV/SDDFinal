import numpy as np


def GA_Planete(nmax, dim, pr, pm):
    #nmax este numarul maxim de iteratii
    #dim este dimensiunea populatiei
    #pr este algoritmul de recombinare
    #pm este algoritmul de mutatie
    i=0
    populatie=generare_populatie(dim)
    while i<nmax:
        #parinti=selectie_parinti_SUS(populatie)
        #desc1=recombinare_uniPunct(parinti)
        #desc2=mutatie_prinNegare(desc1)
        #generatieViitoare=selectie_elitista(desc2)
        i=i+1
    x=np.argsort(populatie[:,-1])

#Populatie initiala este generata prin agoritmul GenPop
#Din aceasta populatie sunt selectati prin metoda SUS cei mai buni parinit, candidati la solutie
#Acesti candidati la solutie sunt recombinati pentru obtinearea de copii, in cazul unui individ(copil)aberant, se va pastra parintele
#Dupa generarea copiilor, acestia sunt negati in algoritmul de mutati pentru generare de indivizi noi
#Generatie viitoare este formata din parinti si copii, cei mai buni, alesi prin metoda Elitista
#Buca while functioneaza pana cand numarul de iteratii se termina i=nmax
#Vectorul x este ordonat crescator dupa ultima coloana(cea a calitatii)-->pentru a obtine candidatul slutie cel mai bun

def generare_populatie(dim):
    populatie=np.zeros(dim, dtype=int)
    populatie[:,-1]=f_obiectiv(populatie)

#algoritmul de generare a populatiei va initializa ultimul element al fiecarui individ cu calitatea sa,
# obtinuta prin functia fitness

def f_obiectiv(n):
    #se va calcula calitatea fiecarui individ prin insumarea importanetei fiecarui individ
    #importantele fiecarei planete vor fi citite dintr-un fisiser text
    return n
#la final aceasta functie v-a returna calitatea