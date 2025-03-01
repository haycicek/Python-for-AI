def hesap_makinesi(sayi1, sayi2, islem):
    if islem == "+":
        result = sayi1 + sayi2
        print(f"{sayi1} + {sayi2} = {result}")
        return
    elif islem == "-":
        result = sayi1 - sayi2
        print(f"{sayi1} - {sayi2} = {result}")
        return
    elif islem == "*":
        result = sayi1 * sayi2
        print(f"{sayi1} * {sayi2} = {result}")
        return
    elif islem == "/":
        if sayi2 != 0:
            result = sayi1 / sayi2
            print(f"{sayi1} / {sayi2} = {result}")
            return
        else:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
            return
    else:
        print("Geçersiz işlem türü!")

try:
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    islem = input("İşlem türünü seçin (+, -, *, /): ")
    hesap_makinesi(sayi1, sayi2, islem)
except ValueError:
    print("Lütfen geçerli bir sayı girin!")