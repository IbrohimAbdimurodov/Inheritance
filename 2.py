class Odam:
    def __init__(self, ismi, familiya, yoshi):
        self.ismi = ismi
        self.familiya = familiya
        self.yoshi = yoshi
    
    def shifr(self):
        print(self.ismi, self.familiya, self.yoshi)

class Student(Odam):
    def __init__(self, ismi, familiya, yoshi, inst, kasbi):
        super().__init__(ismi, familiya, yoshi)
        self.inst = inst
        self.kasbi = kasbi

    def shifr(self):
        print("Ismi:", self.ismi,"Familiyasi:", self.familiya,"Yoshi:", self.yoshi,"Inst:", self.inst,"Kasbi:", self.kasbi)

o1 = Student("Aziz", "Bahronov", "18", "TATU", "Dasturchi")



class Dasturchi(Odam):
    def __init__(self, ismi, familiya, yoshi, prog, github ):
        super().__init__(ismi, familiya, yoshi)
        self.prog = prog
        self.github = github

    def shifr(self):
        print("Ismi:", self.ismi, "Familiyasi:", self.familiya, "Yoshi:" ,self.yoshi, "Prog:" ,self.prog, "GitHub:", self.github)


d1 = Dasturchi("Sardor", "Shomurodov", "21", "Python","SardorShomurodv")



class Futbolchi(Odam):
    def __init__(self, ismi, familiya, yoshi, komandasi, davlat):
        super().__init__(ismi, familiya, yoshi)
        self.komandasi = komandasi
        self.davlat = davlat

    def shifr(self):
        print("Ismi:", self.ismi, "Familiyasi:", self.familiya,"Yoshi:", self.yoshi,"Komandasi:", self.komandasi,"Davlati:", self.davlat)

f1 = Futbolchi("Ozod", "Alisherov", "20", "Qizilqum", "Uzb")

f1.shifr()
d1.shifr()
o1.shifr()
