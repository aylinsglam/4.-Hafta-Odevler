x=list()
y=list()
demet=(1,1,1,2,2,3,3,"Mustafa","Mustafa",3.14,3.14)
for i in demet:
    x.append(i)
print(x)
for i in range(0,len(x)):
    if x[i] not in y:
        y.append(x[i])
print(y)
        



