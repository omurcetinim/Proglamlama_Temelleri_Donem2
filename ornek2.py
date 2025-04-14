park_sure=int(input("Otoparkta duracağınız dakikayı giriniz: "))
if park_sure <=60:
    print("Ücret=5 TL")
elif park_sure <=300:
    print("Ücret",(park_sure/60*4))
else:
    print("Ücret",(park_sure/60*3))