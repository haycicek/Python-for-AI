def asal_mi(sayi):
    if sayi < 2:
        print(f"{sayi} bir asal sayı değildir.")
        return
    for k in range(2, sayi):
        if sayi % k == 0:
            print(f"{sayi} bir asal sayı değildir.")
            return
    print(f"{sayi} bir asal sayıdır.")

asal_mi(7)  # Çıktı: 7 bir asal sayıdır.
asal_mi(10) # Çıktı: 10 bir asal sayı değildir.
asal_mi(222222)
asal_mi(13)
