a=dict()
z=list()
y=list()
string=input("Stringi giriniz: ")
x=list(string)

for i in range(0,len(x)):
    if x[i] not in y:
        y.append(x[i])

for j in range(0,len(y)):
    b=x.count(y[j])
    z.append(b)
    a.update({y[j]:z[j]})
print(a)
