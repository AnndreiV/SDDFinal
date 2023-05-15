"3. Sunt consideraqte cunoscute 2 secvente de numere natural, X=(x1,x2,…,xn) si Y=(y1,y2,….,yn)."
"Utilizati un algoritm genetic pentru a determina, daca exista, o aranjare a vectorului Y intr-un nou vector Z=(z1,z2,…,zn) astfel incat, pentru orice component I,"
"zi=a*xi+b, a si b numere natural date."
import numpy
X=[3,6,9]
Y=[3,4,5]
a=1
b=2
def fitness(Z):
    scor = 0
    n=len(X)
    for i in range(n):
        if (Z[i] == a * X[i] + b):
            scor += 1
    if (len(Z) != len(X)):
        scor = 0

    return scor


def generare(dim):
    populatie = []
    calitati = []

    for i in range(dim):
        "Amesteca permutarea Y"
        Z = numpy.random.permutation(Y)
        populatie += [Z]
        calitati += [fitness(Z)]
    return numpy.asarray(calitati), numpy.asarray(populatie)


