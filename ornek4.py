zayif_sayisi= []
toplam= 0
for i in range(6):
    zayif_sayisi.append(int(input("Ders notunuzu giriniz: ")))
for j in zayif_sayisi:
    toplam=toplam+j
    if j>50:
        zayif_sayisi=zayif_sayisi+1
ortalama=toplam/6
print( "Ortalamanz: ",ortalama)
print("Kaldığınız ders sayısı: ",zayif_sayisi)