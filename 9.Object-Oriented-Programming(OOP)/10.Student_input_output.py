class Student:
    def __init__(self, ten, tuoi, mssv):
        self.ten = ten
        self.tuoi = tuoi
        self.mssv = mssv
    
    def nhap_thong_tin(self):
        self.ten = input("Nhap ten: ")
        self.tuoi = int(input("Nhap tuoi: "))
        self.mssv = input("Nhap MSSV: ")
    
    def in_thong_tin(self):
        print(f"Ten: {self.ten}, Tuoi: {self.tuoi}, MSSV: {self.mssv}")

sv = Student("", 0, "")
sv.nhap_thong_tin()
sv.in_thong_tin()
