a=int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz: "))
c=input("yapmak istediğiniz işlemi giriniz: ")
b=int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz: "))

while c=="+" or c=="-" or c=="/" or c=="*":
    if c=="+":
        print("işlemnizin sonucu: " , a+b)
        a=int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz: "))
        c=input("yapmak istediğiniz işlemi giriniz: ")
        b=int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz: "))
    elif c=="-":
        print("işleminizin sonucu: ", a-b)
        a=int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz: "))
        c=input("yapmak istediğiniz işlemi giriniz: ")
        b=int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz: "))
    elif c=="/":
        print("işleminizin sonucu: ", a/b)
        a=int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz: "))
        c=input("yapmak istediğiniz işlemi giriniz: ")
        b=int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz: ")) 
    elif c=="*":
        print("işleminizin sonucu: ", a*b)
        a=int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz: "))
        c=input("yapmak istediğiniz işlemi giriniz: ")
        b=int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz: "))
else:
    print("Geçerli bir işlem girmediniz")
            
    
