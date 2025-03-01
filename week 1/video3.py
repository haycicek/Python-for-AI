class Human:
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

human1 = Human("İbrahim")
human1.talk("Merhabalar")
human1.walk()
print(human1)


human2 = Human("ali")
human2.talk("naber")
human2.walk()
print(human2)
