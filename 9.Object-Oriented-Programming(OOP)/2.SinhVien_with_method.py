class SinhVien:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    
    def in_thong_tin(self):
        print(f"Ten: {self.ten}, Tuoi: {self.tuoi}")

sv = SinhVien("Nguyen Thi B", 22)
sv.in_thong_tin()