print("kodlamaio")

# degiskenAdi = deger (int, float, string, boolean)
baslik = "Araba Kredisi"  # string => metinsel ifade

print(baslik)

baslik = "İhtiyaç Kredisi"  # string => metinsel ifade

print(baslik)

vade = 36  # int => tam sayı
ekVade = 6  # int => tam sayı

vade2 = "36"  # string => metinsel ifade

aylikOdeme = 200.50  # float => ondalıklı sayı

zamYapildiMi = True  # boolean => doğru veya yanlış

# Matematiksel Operatörler

# + => toplama
print(5 + 5)  # 10
print(vade + 12)  # 48
print(vade + ekVade)  # 42
print(36 + 6)  # 42

# - => çıkarma
print(5 - 5)  # 0
print(vade - 12)  # 24
print(vade - ekVade)  # 30
print(36 - 6)  # 30

# * => çarpma
print(5 * 5)  # 25
print(vade * 12)  # 432
print(vade * ekVade)  # 216
print(10 * 10)  # 100

# / => bölme
print(5 / 5)  # 1.0
print(vade / 2)  # 18.0
print(vade / ekVade)  # 6.0
print(10 / 2)  # 5.0

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)  # 18.0
print(indirimliFiyat)  # 80

# % => mod (kalanı bulma)
print(10 % 2)  # 0
print(vade % 5)  # 1
print(vade % ekVade)  # 0
print(30 % 10)  # 0

# Mantıksal Operatörler

# == => eşit mi?
print(1 == 1)  # True (Doğru)
print(1 == 2)  # False (Yanlış)

# > => büyük mü?
print(1 > 2)  # False
print(3 > 1)  # True
print(1 > 1)  # False
print(1 >= 1)  # True (Büyük veya eşit mi?)

# < => küçük mü?
print(1 < 2)  # True
print(3 < 1)  # False
print(1 < 1)  # False
print(1 <= 1)  # True (Küçük veya eşit mi?)

# != => eşit değil mi?
print(1 != 1)  # False
print(1 != 2)  # True

# or => veya (Biri doğruysa sonuç doğru olur)
print(1 > 2 or 5 > 2)  # (Yanlış veya Doğru) => True
print(1 > 2 or 5 > 2 and 3 > 2)  # (Yanlış veya Doğru ve Doğru) => True
print(1 > 2 and 5 > 2 and 3 > 2)  # (Yanlış ve Doğru ve Doğru) => False
print(2 > 1 or 1 > 2 and 3 > 2)  # (Doğru veya Yanlış ve Doğru) => True

# and => ve (Her iki koşul da doğru olmalı)
print(1 > 2 and 5 > 2)  # (Yanlış ve Doğru) => False

# If Koşulu

# if koşul:
#     kod bloğu

sayi1 = 15
sayi2 = 15

if sayi1 < sayi2:
    print("sayi1, sayi2'den küçüktür.")
    print("if bloğunun içi")
elif sayi1 == sayi2:
    print("sayi1, sayi2'ye eşittir.")
    print("elif bloğunun içi")
else:
    print("sayi2, sayi1'den büyüktür.")
    print("else bloğunun içi")

print("if bloğunun dışı")

if sayi1 <= sayi2:
    print("sayi1, sayi2'ye küçük veya eşittir.")
if sayi1 == sayi2:
    print("sayi1, sayi2'ye eşittir.")
else:
    print("sayi2, sayi1'den büyüktür.")

# Sonuç => sayi1, sayi2'ye küçük veya eşittir, sayi1 sayi2'ye eşittir.

if sayi1 < sayi2:
    print("sayi1, sayi2'den küçüktür.")
    if sayi1 == sayi2:
        print("sayi1, sayi2'ye eşittir.")
else:
    print("sayi2, sayi1'den büyüktür.")

# Sonuç => sayi2, sayi1'den büyüktür.
