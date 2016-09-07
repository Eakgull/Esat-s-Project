defsayi =("5")

while (True):
    sayi = input("Lütfen sayıyı tahmin edin:")
    if ((sayi == defsayi)):
        print("Doğru Tahmin")
        break
    elif ((sayi != defsayi)):
        print("Tekrar Deneyin")
        input()
   
