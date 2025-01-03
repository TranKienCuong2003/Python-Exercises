class Person:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

class Student(Person):
    def __init__(self, ten, tuoi, mssv):
        super().__init__(ten, tuoi)
        self.mssv = mssv
    
    def in_thong_tin(self):
        print(f"Ten: {self.ten}, Tuoi: {self.tuoi}, MSSV: {self.mssv}")

sv = Student("Nguyen Thi C", 21, "SV12345")
sv.in_thong_tin()
