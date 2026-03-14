class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        if 2 <= value <= 5:
            self.__grade = value
        else:
            print(f"BŁĄD: {value} to nie jest ocena w Polsce, ziomek.")

    @staticmethod
    def is_valid_email(email):
        if "@" in email:
            return True
        return False
    
    @classmethod
    def from_string(cls, data_string):
        name, grade = data_string.split("-")
        grade = int(grade)
        return cls(name, grade)
    
    def __str__(self):
        return f"Student {self.name} has grade {self.grade}"
    

    # 1. Test metody statycznej (bez tworzenia obiektu!)
print(Student.is_valid_email("test@uek.krakow.pl")) # True

# 2. Test metody klasy (tworzenie z napisu)
s1 = Student.from_string("Jan-5")
print(s1) # [Student] Imię: Jan, Ocena: 5

# 3. Test walidacji (z poprzednich lekcji)
s1.grade = 6 # Ma wypisać błąd
    


