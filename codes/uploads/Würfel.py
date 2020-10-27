import random
anzahl=int(input('Anzahl der Würfel: '))
k=0
while k==0:
    input()
    ergebnis=[]
    for i in range(anzahl):
        x=random.randint(1,6)
        ergebnis.append(x)
    print(ergebnis)