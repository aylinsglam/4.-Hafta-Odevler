sifre=input("Lütfen şifrenizi giriniz: ")
while len(sifre)!=4 or sifre.isdigit()==False:
    sifre=input("Lütfen 4 haneli ve rakamlardan oluşan bir şifre giriniz: ")
else:
    print("yeni şifreniz: " , sifre)
