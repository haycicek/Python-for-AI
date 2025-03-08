metin = input("Input: ")
with open("metin.txt", "w", encoding="utf-8") as dosya:
    dosya.write(metin)

print("\nmetin.txt dosyasının içeriği:")
with open("metin.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())

print("\n5 farklı satır girin:")
with open("satirlar.txt", "a", encoding="utf-8") as dosya:
    for i in range(5):
        satir = input(f"{i + 1}. Satır: ")
        dosya.write(satir + "\n")

print("\nsatirlar.txt dosyasının içeriği:")
with open("satirlar.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        print(satir.strip())
