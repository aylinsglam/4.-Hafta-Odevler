liste=[3,6,4,1,10,12,-1,2,-20]
yeni_liste=list()
for i in range(0,len(liste)):
    a=min(liste)
    #listenin en küçük elemanını buldum
    b=liste.index(a)
    #en küçük elemanın indisini buldum
    c=liste.pop(b)
    #listenin en küçük elemanını listeden sildim
    yeni_liste.append(c)
print(yeni_liste)
    
    
