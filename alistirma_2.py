x=list()
demet=(2,3,4,3.14,"Mustafa",132,"Kemal","Atatürk",5)
for i in demet:
    x.append(i)
for i in range(0,len(x)):
    if type(x[i])==str:
        print(x[i])



