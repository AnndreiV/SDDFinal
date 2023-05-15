import numpy as np

def fitness(bv, individ,n):
    m = len(individ)
    v = np.zeros(n)
    v=list(v)
    for i in range(m):
        v[individ[i]]=v[individ[i]]+bv[i]
    scor2 = 0
    media=0
    for i in range(n):
        media=media+v[i]
    media=media/n
    for i in range(n):
        scor2=scor2+abs(v[i]-media)
    scor=1/(1+scor2)
    return scor

def gen(fg, n, dim):
    b = np.genfromtxt(fg)
    b[1]=list(b[1])
    individ=[]
    pop=[]
    scoruri_pop=[]
    m = len(b[0])
    for i in range(dim):
        individ=np.random.randint(0,n,m)
        individ=list(individ)
        pop=pop+[individ]
        scoruri_pop=scoruri_pop+[fitness(b[1], individ, n)]
    return np.asarray(pop), np.asarray(scoruri_pop)

"""def GA(dim, fg, n, NMAX, pc, pm):

    b=np.genfromtxt(fg)
    b=list(b)
    pop_init, scor_init = gen(fg,n, dim)
    istoric_maxime=max(scor_init)
    m = len(pop_init[0])
    gata = False
    if istoric_maxime == 1:
        gata= True
    iteratie = 1
    pop = pop_init
    sco = scor_init
    nrm=0

    while iteratie <= NMAX and not gata:
        pop_intermediara = []
        scor_intermediar = []
        parinti_selectati, scoruri_parinti = FS.ruleta(pop,sco, dim, m)
        for i in range(0,dim-1,2):
            parinte1=parinti_selectati[i]
            parinte2=parinti_selectati[i+1]
            k=np.random.uniform(0,1)
            if k<=pc:
                copil1, copil2 = FC.crossover_uniform(parinte1, parinte2, n)
            else:
                copil1 = parinte1
                copil2 = parinte2
            k=np.random.uniform(0,1)
            if k<=pm:
                gena=np.random.randint(0,m)
                copil1[gena]=FM.m_fluaj(gena, 0, n-1)
            k=np.random.uniform(0,1)
            if k<=pm:
                gena=np.random.randint(0,m)
                copil2[gena]=FM.m_fluaj(gena, 0, n-1)
            pop_intermediara=pop_intermediara+[copil1]
            pop_intermediara = pop_intermediara + [copil2]
            scor_intermediar=scor_intermediar+[fitness(b[1],copil1,n)]
            scor_intermediar = scor_intermediar + [fitness(b[1], copil2, n)]

        pop_urmatoare, scor_urmatoare=FS.elitism(parinti_selectati, scoruri_parinti, pop_intermediara, scor_intermediar, dim)

        if max(scor_urmatoare) == 1:
            gata=True
        if max(scor_urmatoare)<=istoric_maxime:
            nrm=nrm+1
        else:
            nrm=0
        if nrm>NMAX/3:
            gata=True
        istoric_maxime=max(scor_urmatoare)
        iteratie=iteratie+1

    print(scor_urmatoare)
    solutie=[]
    scor_solutie=max(scor_urmatoare)
    for i in range(dim):
        if scor_urmatoare[i]==scor_solutie:
            solutie=pop_urmatoare[i]


    return solutie, scor_solutie"""


